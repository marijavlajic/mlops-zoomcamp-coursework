import os
import mlflow

print(f'mlflow version is {mlflow.__version__}')

file_size = os.path.getsize('./output/dv.pkl')/1024

print(f'Size of dv.pkl file is {file_size} kb')