import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Définir les chemins d'accès
raw_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
raw_data_file = os.path.join(raw_data_path, 'rawdata.csv')

def download_data(dataset, save_path):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=save_path, unzip=True)
    print(f"Données téléchargées et enregistrées dans {save_path}")

def rename_file(downloaded_file, new_file_path):
    if os.path.exists(downloaded_file):
        if os.path.exists(new_file_path):  # Vérifiez si le fichier de destination existe
            os.remove(new_file_path)       # Supprimez-le si c'est le cas
        os.rename(downloaded_file, new_file_path)
        print(f"Fichier renommé en {new_file_path}")
    else:
        print(f"Fichier téléchargé introuvable: {downloaded_file}")

# Identifiant du jeu de données Kaggle
dataset = "kumarajarshi/life-expectancy-who"

# Vérifier si le répertoire existe
os.makedirs(raw_data_path, exist_ok=True)

# Télécharger les données
download_data(dataset, raw_data_path)

# Renommer le fichier téléchargé en 'rawdata.csv'
downloaded_file = os.path.join(raw_data_path, "Life Expectancy Data.csv")
rename_file(downloaded_file, raw_data_file)
