import h5py
import json
import shutil

model_path = "models/lung_cancer_model_final.h5"
fixed_path = "models/lung_cancer_model_fixed.h5"

shutil.copy(model_path, fixed_path)
print("Copied model...")

with h5py.File(fixed_path, 'r+') as f:
    config = f.attrs['model_config']
    if isinstance(config, bytes):
        config = config.decode('utf-8')
    
    config_dict = json.loads(config)
    config_str = json.dumps(config_dict)
    
    # Fix batch_shape
    config_str = config_str.replace('"batch_shape"', '"batch_input_shape"')
    
    # Fix DTypePolicy - replace object dtype with simple string
    config_str = config_str.replace(
        '{"module": "keras", "class_name": "DTypePolicy", "config": {"name": "float32"}, "registered_name": null}',
        '"float32"'
    )
    
    f.attrs['model_config'] = config_str.encode('utf-8')

print("✅ Model fully fixed! Saved as models/lung_cancer_model_fixed.h5")
