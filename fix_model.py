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
    config_str = config.replace('"batch_shape"', '"batch_input_shape"')
    f.attrs['model_config'] = config_str.encode('utf-8')

print("Model fixed and saved as models/lung_cancer_model_fixed.h5")
