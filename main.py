import plotly.io  
import webbrowser
from src.utils.get_data import load_cleaned_data

# Charger les données nettoyées
data = load_cleaned_data()

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
"""
from src.components.carte import carte
if data is not None:
    car = carte(data)
    webbrowser.open(carte)
else:
    print("Pas possible d'afficher la carte")
"""
from src.pages.DASH1 import create_dashboard

# Appeler la fonction pour démarrer le dashboard
create_dashboard()