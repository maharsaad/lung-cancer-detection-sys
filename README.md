# Lung Cancer Detection System

An AI-powered web application that classifies histopathological lung tissue images into **adenocarcinoma**, **benign**, or **squamous cell carcinoma** using a Convolutional Neural Network (CNN), with a Flask-based web interface for real-time predictions.

## Overview

Early and accurate detection of lung cancer significantly improves treatment success and survival rates. Manual histopathological image analysis is labor-intensive, time-consuming, and susceptible to human error. This project overcomes these challenges with an AI-powered automated system that classifies lung tissue images, reducing diagnostic delays and improving clinical decision-making — paired with a simple web interface so medical professionals can upload an image and get an instant, confidence-scored diagnosis.

## Problem Statement

Traditional manual analysis of histopathological images is labor-intensive and prone to error. This project develops an automated, AI-powered system capable of accurately analyzing and classifying lung tissue images to support faster, more reliable diagnosis.

## Scope

- Upload and process histopathological images of lung tissue
- Perform real-time classification into adenocarcinoma, benign, or squamous cell carcinoma
- Display confidence scores indicating prediction certainty
- Offer detailed visual analysis of results to assist interpretation
- Present model performance metrics for transparency and evaluation

## Objectives

- Develop a robust deep learning model to accurately classify lung cancer subtypes
- Design an intuitive web-based interface for image submission and result visualization
- Enable real-time image processing for immediate diagnostic feedback
- Provide comprehensive analysis and confidence metrics alongside predictions
- Ensure high accuracy, reliability, and clinical relevance

## Features

- Upload histopathological lung tissue images via drag-and-drop or file picker
- Real-time classification into 3 categories: adenocarcinoma, benign, squamous cell carcinoma
- Confidence score displayed alongside prediction
- "See More" panel showing training accuracy/loss graphs for transparency
- Responsive, modern web UI

## Tech Stack

- **Model:** TensorFlow / Keras (CNN)
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Image Processing:** Pillow (PIL), NumPy
- **Environment:** Tested on macOS (M1) with `tensorflow-macos==2.13.0`, `keras==2.13.1`, `pillow==9.5.0`, Python 3.11

## Project Structure
<img width="465" height="308" alt="Screenshot 2026-06-28 at 4 21 29 PM" src="https://github.com/user-attachments/assets/fb605616-5a9f-4eab-bc48-a9acd2dc6b9f" />

## Methodology

### Deep Learning Model
- Convolutional Neural Network (CNN) architecture tailored for image classification
- Data augmentation techniques (rotation, flipping, zoom, contrast, brightness) to enhance generalization
- Trained on a curated dataset of annotated histopathological lung tissue images
- Validated through accuracy, precision, recall, and F1-score

### Web Application
- Built with Flask for backend processing
- Modern, responsive front-end for image submission and result visualization
- Real-time image upload and classification
- Interactive display of classification results and confidence scores

## Model Architecture

Base classification model:

```python
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(192, 192, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])
```

The training notebook (`trainedModel.ipynb`) uses a deeper variant with `BatchNormalization`, `GlobalAveragePooling2D`, and heavier data augmentation, trained for up to 25 epochs with early stopping and learning-rate reduction callbacks:

```python
model = Sequential([
    Rescaling(1.0 / 255, input_shape=(224, 224, 3)),
    Conv2D(32, (3, 3), activation="relu", padding="same"),
    MaxPooling2D((2, 2)),
    BatchNormalization(),
    Dropout(0.25),
    Conv2D(64, (3, 3), activation="relu", padding="same"),
    MaxPooling2D((2, 2)),
    BatchNormalization(),
    Dropout(0.3),
    Conv2D(128, (3, 3), activation="relu", padding="same"),
    MaxPooling2D((2, 2)),
    BatchNormalization(),
    Dropout(0.3),
    Conv2D(256, (3, 3), activation="relu", padding="same"),
    MaxPooling2D((2, 2)),
    BatchNormalization(),
    Dropout(0.4),
    GlobalAveragePooling2D(),
    Dense(512, activation="relu"),
    Dropout(0.5),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(3, activation="softmax"),
])
```

**Training configuration:**
- Optimizer: Adam (learning rate 0.001)
- Loss: Sparse categorical crossentropy
- Callbacks: EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
- Epochs: up to 25

## Web Interface

The web app features a clean, intuitive interface for uploading histopathological lung tissue images. Once uploaded, the image is processed by the AI model and results are displayed in real-time, including a "See More" section with training accuracy/loss graphs and the confidence score.

### Upload Page
<img width="1025" height="808" alt="Screenshot 2026-06-28 at 4 24 47 PM" src="https://github.com/user-attachments/assets/eebcbda6-3527-494a-9fb6-67bf0ed881f0" />


### Prediction Result
<img width="572" height="794" alt="Screenshot 2026-06-28 at 4 26 03 PM" src="https://github.com/user-attachments/assets/47225022-6789-48f8-9165-1b3836146f68" />


### Model Training Performance
<img width="850" height="780" alt="Screenshot 2026-06-28 at 4 26 23 PM" src="https://github.com/user-attachments/assets/5118f875-5c74-49df-a17e-ee6f558359f6" />


## How to Run

1. Navigate to the project folder:
```bash
   cd ~/Desktop/Lung_cancer_detection_sys
```

2. Activate the conda environment (create it first if it doesn't exist):
```bash
   conda activate lung_cancer
```

   If you don't have the environment set up yet:
```bash
   conda create -n lung_cancer python=3.11
   conda activate lung_cancer
   pip install tensorflow-macos==2.13.0 keras==2.13.1 pillow==9.5.0 flask numpy
```

3. Run the Flask app:
```bash
   python app.py
```

4. Open your browser and go to:
<img width="217" height="52" alt="Screenshot 2026-06-28 at 4 21 52 PM" src="https://github.com/user-attachments/assets/bc812689-1e0c-46d8-9bb9-dd2db062dacb" />

## API

### `POST /predict`
Accepts a form-data image upload under the `image` field.

**Response:**
```json
{
  "prediction": "adenocarcinoma",
  "confidence": "94.32%"
}
```

**Error response example:**
```json
{
  "error": "No image uploaded"
}
```

## Conclusion

The Lung Cancer Detection System successfully demonstrates the application of deep learning techniques in medical diagnostics by providing an accurate and efficient AI-powered classification tool. The system combines a robust CNN model with a user-friendly web interface to facilitate rapid lung cancer detection, assisting medical professionals in early diagnosis and improving patient outcomes. This project validates the potential of integrating AI technologies into clinical workflows to enhance diagnostic accuracy and accessibility.

## Future Work

- Integration with existing medical imaging and electronic health record (EHR) systems
- Expansion of the model to classify additional lung cancer subtypes and pulmonary diseases
- Development of a mobile application for accessibility in remote areas
- Incorporation of patient history and medical records for personalized diagnostics
- Real-time collaboration features for multiple medical professionals
- Training on larger and more diverse datasets for improved accuracy
- Explainable AI techniques for transparent, trustworthy predictions

## Tools Used

- Python, TensorFlow / Keras
- Flask
- HTML / CSS / JavaScript
- VS Code

## Author

Mahar Saad  
GitHub: https://github.com/maharsaad
