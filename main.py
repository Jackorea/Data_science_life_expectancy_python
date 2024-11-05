from src.utils.get_data import load_cleaned_data

# Charger les données nettoyées
data = load_cleaned_data()

if data is not None:
    print(data.head())  # Pour vérifier que les données sont bien chargées
else:
    print("Erreur lors du chargement des données.")

from src.components.component2 import create_life_expectancy_chart

# Charger les données nettoyées
data = load_cleaned_data()

if data is not None:
    fig = create_life_expectancy_chart(data)
    fig.show()  # Affiche le graphique si vous êtes dans un environnement supportant les visualisations
else:
    print("Erreur lors du chargement des données.")