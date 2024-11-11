import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Définir les chemins d'accès
raw_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
raw_data_file = os.path.join(raw_data_path, 'rawdata.csv')

def download_data(dataset, save_path):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=save_path, unzip=True)
    print(f"Data downloaded and saved to {save_path}")

def rename_file(downloaded_file, new_file_path):
    if os.path.exists(downloaded_file):
        os.rename(downloaded_file, raw_data_file)
        print(f"File renamed to {raw_data_file}")
    else:
        print(f"Downloaded file not found: {downloaded_file}")


dataset = "kumarajarshi/life-expectancy-who"  # Kaggle dataset identifier

# Ensure the directory exists
os.makedirs(raw_data_path, exist_ok=True)

# Download data
download_data(dataset, raw_data_path)

# Rename the downloaded file to 'rawdata.csv'
downloaded_file = os.path.join(raw_data_path, "Life Expectancy Data.csv")  # Adjust this if the file name is different
rename_file(downloaded_file, raw_data_file)