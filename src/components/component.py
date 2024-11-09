import pandas as pd
import plotly.express as px

def life_expectancy_percentage_expenditure_2010_paysnodev(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    yearDeveloping = data.query("Year==2010 and Status=='Developing'")
    
    fig = px.scatter(
        yearDeveloping,
        x='Life expectancy ',
        y='Diphtheria ',
        hover_name='Country',  # Ajoute le nom des pays lors du survol
        labels={
            'Life expectancy ': 'Espérance de vie',
            'Diphtheria ': ' impact campagne vaccin'
        },
        title="Espérance de vie vs l'inpact les campagne de vaccin pour les pays en développement (2010)"
    )

    fig.update_traces(marker=dict(size=10))  # Ajuste la taille des points si nécessaire
    fig.update_layout(
        xaxis_title="Espérance de vie",
        yaxis_title="Diphtheria "
    )

    return fig

def life_expectancy_percentage_expenditure_2010_paysdev(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    yearDeveloped = data.query("Year==2010 and Status=='Developed'")
    
    fig = px.scatter(
        yearDeveloped,
        x='Life expectancy ',
        y='Diphtheria ',
        hover_name='Country',  # Ajoute le nom des pays lors du survol
        labels={
            'Life expectancy ': 'Espérance de vie',
            'Diphtheria ': 'Campagne vaccinale'
        },
        title="Espérance de vie vs campagne vaccinale pour les pays développés (2010)"
    )

    fig.update_traces(marker=dict(size=10))  # Ajuste la taille des points si nécessaire
    fig.update_layout(
        xaxis_title="Espérance de vie",
        yaxis_title="campagne vaccinale"
    )

    return fig
