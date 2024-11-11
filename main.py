import plotly.io
import pandas as pd
import os
import webbrowser
from src.utils.clean_data import clean_data, load_cleaned_data, load_raw_data, save_cleaned_data, raw_data_path, cleaned_data_path
from src.utils.get_data import download_data, rename_file

# Définir les chemins d'accès
#raw_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')

# Define the dataset and save path
dataset = "kumarajarshi/life-expectancy-who"
raw_data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
#raw_data_path = os.path.join(os.path.dirname(__file__), 'data', 'raw')
#raw_data_dir = os.path.join(os.path.dirname(__file__), 'data', 'raw')
#raw_data_file = os.path.join(raw_data_path, 'rawdata.csv')
raw_data_file = os.path.join(raw_data_dir, 'rawdata.csv')
os.makedirs(raw_data_dir, exist_ok=True)

# Download the data
#download_data(dataset, raw_data_path)
download_data(dataset, raw_data_dir)


# Rename the downloaded file to 'rawdata.csv'
downloaded_file = os.path.join(raw_data_dir, "Life Expectancy Data.csv")  # Adjust this if the file name is different
rename_file(downloaded_file, raw_data_file)

# Load, clean, and save the data
raw_data = load_raw_data()
if raw_data is not None:
    cleaned_data = clean_data(raw_data)
    save_cleaned_data(cleaned_data)

# Charger les données nettoyées
data = load_cleaned_data()
from src.pages.DASH1 import create_dashboard
if data is not None:
    print(data.head())  # Pour vérifier que les données sont bien chargées
else:
    print("Erreur lors du chargement des données.")


if __name__ == "__main__":
    create_dashboard() #démarrer le dashboard