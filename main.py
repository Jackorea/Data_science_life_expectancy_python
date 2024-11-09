import plotly.io
import pandas as pd
import os
import webbrowser
from src.utils.get_data import load_cleaned_data
from src.utils.clean_data import clean_data, raw_data_path, cleaned_data_path

# Charger les données non-nettoyées
raw_data = pd.read_csv(raw_data_path)

# nettoyer les données
cleaned_data = clean_data(raw_data)

# Save the cleaned data
os.makedirs(os.path.dirname(cleaned_data_path), exist_ok=True)
cleaned_data.to_csv(cleaned_data_path, index=False)

print(f"Cleaned data saved to {cleaned_data_path}")

# Charger les données nettoyées
data = load_cleaned_data()
from src.pages.DASH1 import create_dashboard
if data is not None:
    print(data.head())  # Pour vérifier que les données sont bien chargées
else:
    print("Erreur lors du chargement des données.")

# Appeler la fonction pour démarrer le dashboard
if __name__ == "__main__":
    create_dashboard()
"""
if data is not None:
    print(data.head())  # Pour vérifier que les données sont bien chargées
else:
    print("Erreur lors du chargement des données.")

from src.components.component3 import life_expectancy_expenditure

# Charger les données nettoyées
data = load_cleaned_data()

if data is not None:
    fig = life_expectancy_expenditure(data)
    #fig.show()  # Affiche le graphique si vous êtes dans un environnement supportant les visualisations
    plotly.io.write_html(fig, file='fig.html', auto_open=True, include_plotlyjs='cdn')
else:
    print("Erreur lors du chargement des données.")

from src.components.carte import carte
if data is not None:
    car = carte(data)
    webbrowser.open(carte)
else:
    print("Pas possible d'afficher la carte")

from src.pages.DASH1 import create_dashboard

# Appeler la fonction pour démarrer le dashboard
create_dashboard()
"""