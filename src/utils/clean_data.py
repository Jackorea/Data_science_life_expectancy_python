import pandas as pd
import os

# Définir les chemins d'accès
raw_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw', 'rawdata.csv')
cleaned_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned', 'cleaneddata.csv')

# Charger les données non-nettoyés
raw_data = pd.read_csv(raw_data_path)

def clean_data(raw_data):
    # Supprimer les doublons
    cleaned_data = raw_data.drop_duplicates()

    # Gérer les valeurs manquantes en utilisant la moyenne de chaque pays
    for column in cleaned_data.columns:
        if cleaned_data[column].dtype in ['int64', 'float64']:
            cleaned_data[column] = cleaned_data.groupby('Country')[column].transform(lambda x: x.fillna(x.mean()))

    # Convertir la colonne 'Year' en entier
    if 'Year' in cleaned_data.columns:
        cleaned_data['Year'] = cleaned_data['Year'].astype(int)

    # Remove rows where 'Country' is 'Tuvalu' or 'Marshall Islands'
    cleaned_data = cleaned_data[~cleaned_data['Country'].isin(['Tuvalu', 'Marshall Islands'])]

    # Update 'Status' column to 'Developed' for specific countries
    developed_countries = [
        'France', 'Republic of Korea', 'Canada', 'Israel', 'Finland', 'Qatar',
        'United Arab Emirates', 'Saudi Arabia', 'Kuwait', 'Greece', 'Estonia'
    ]
    cleaned_data.loc[cleaned_data['Country'].isin(developed_countries), 'Status'] = 'Developed'

    print("Data cleaning complete.")
    return cleaned_data

# Nettoyer les données
cleaned_data = clean_data(raw_data)

# Sauvegarder les données nettoyées
os.makedirs(os.path.dirname(cleaned_data_path), exist_ok=True)
cleaned_data.to_csv(cleaned_data_path, index=False)
print(f"Cleaned data saved to {cleaned_data_path}")

def load_cleaned_data():
    # Définir le chemin d'accès au fichier nettoyé
    data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned', 'cleaneddata.csv')
    
    # Charger le fichier CSV
    try:
        data = pd.read_csv(data_path)
        print("Données nettoyées chargées avec succès.")
        return data
    except FileNotFoundError:
        print("Le fichier 'cleaneddata.csv' est introuvable.")
        return None