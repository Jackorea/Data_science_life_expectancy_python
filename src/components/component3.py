import plotly.express as px
import pandas as pd

def life_expectancy_expenditure(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    year2008 = data[data['Year'] == 2008]
    fig = px.histogram(
        year2008,
        x='Life expectancy ',
        y='Total expenditure',
        nbins=10,  # Nombre de "bins" ou intervalles pour l'espérance de vie
        title='Histogramme de l\'espérance de vie et des dépenses de santé en 2008',
        labels={'Life expectancy ': 'Espérance de vie', 'Total expenditure': 'Dépenses de santé (% du PIB)'},
        color_discrete_sequence=['#636EFA']
    )
    
    fig.update_layout(
        xaxis_title="Espérance de vie",
        yaxis_title="Dépenses de santé (% du PIB)"
    )

    return fig

"""
def life_expectancy_expenditure(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None

    # Filtrer les données pour l'année 2008
    year2008 = data[data['Year'] == 2008].copy()  # Utilisez .copy() pour éviter les avertissements

    # Définir les intervalles et les étiquettes pour les catégories d'espérance de vie
    bins = [0, 50, 60, 70, 80, 100]
    labels = ["<50 years", "50-60 years", "60-70 years", "70-80 years", ">80 years"]

    # Créer une nouvelle colonne 'Life expectancy category' avec pd.cut
    year2008['Life expectancy category'] = pd.cut(
        year2008['Life expectancy '],
        bins=bins,
        labels=labels,
        right=False
    )

    # S'assurer que les catégories sont bien ordonnées
    year2008['Life expectancy category'] = pd.Categorical(
        year2008['Life expectancy category'],
        categories=labels,
        ordered=True
    )

    # Créer l'histogramme
    fig = px.histogram(
        year2008,
        x='Life expectancy category',
        y='Total expenditure',
        title='Dépenses de santé en fonction des catégories d\'espérance de vie en 2008',
        labels={'Life expectancy category': 'Catégorie d\'espérance de vie', 'Total expenditure': 'Dépenses de santé (% du PIB)'},
        color='Life expectancy category',
        barmode='group'
    )
    
    return fig """
