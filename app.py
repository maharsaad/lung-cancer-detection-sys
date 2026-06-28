import os
import tensorflow as tf
from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image

# ----------------------------
# Flask App Setup
# ----------------------------
app = Flask(__name__, static_folder='static', static_url_path='/static')

# ----------------------------
# Model Path
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models", "lung_cancer_model_fixed.h5")

# ----------------------------
# Load Model
# ----------------------------
model = None

try:
    model = tf.keras.models.load_model(model_path, compile=False)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"Normal load failed: {e}")

    try:
        import h5py

        with h5py.File(model_path, 'r') as f:
            model_config = f.attrs.get('model_config')

            if model_config is not None:
                if isinstance(model_config, bytes):
                    model_config = model_config.decode('utf-8')

                model = tf.keras.models.model_from_json(model_config)
                model.load_weights(model_path)

        print("✅ Model loaded with fallback method!")
    except Exception as e2:
        print(f"Fallback also failed: {e2}")
        model = None

# ----------------------------
# Class Labels
# ----------------------------
class_names = ["adenocarcinoma", "benign", "squamous_cell_carcinoma"]

# ----------------------------
# Image Preprocessing (FIXED)
# ----------------------------
def prepare_image(img):
    img = img.convert("RGB")
    img = img.resize((224, 224))  # ✅ FIXED: must match model input
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        img = Image.open(file.stream)
        img_array = prepare_image(img)

        predictions = model.predict(img_array)

        predicted_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_index]
        confidence = float(np.max(predictions[0]) * 100)

        return jsonify({
            "prediction": predicted_class,
            "confidence": f"{confidence:.2f}%"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------
# Run Server (FIXED PORT ISSUE)
# ----------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,          # ✅ changed from 5000 → 5001
        debug=False,
        use_reloader=False  # ✅ prevents TensorFlow double loading issues
    )
