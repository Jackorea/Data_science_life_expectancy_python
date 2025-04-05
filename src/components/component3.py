import plotly.express as px
import pandas as pd
def histo(data):
    year2008 = data[data['Year'] == 2008]
    fig = px.histogram(
        year2008,
        x='Life expectancy ',
        nbins=10, 
        title="Histogramme de l'espérance de vie en 2008",
        labels={'Life expectancy ': 'Espérance de vie'},
        color_discrete_sequence=['#636EFA'])
    return fig
def histo2(data):
    year2008 = data[data['Year'] == 2015]
    fig = px.histogram(
        year2008,
        x='Life expectancy ',
        nbins=10, 
        title="Histogramme de l'espérance de vie en 2015",
        labels={'Life expectancy ': 'Espérance de vie'},
        color_discrete_sequence=['#636EFA'])
    return fig
 
def life_expectancy_expenditure(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    
    year2008 = data[data['Year'] == 2008]

    fig = px.scatter(
        year2008,
        x='Life expectancy ',
        y='Total expenditure',
        title="Espérance de vie vs Dépenses de santé (2008)",
        labels={
            'Life expectancy ': 'Espérance de vie',
            'Total expenditure': 'Dépenses de santé (% du PIB)'
        },
        color='Status',
        hover_name='Country', 
        template='plotly_white'
    )

    fig.update_layout(
        xaxis_title="Espérance de vie",
        yaxis_title="Dépenses de santé (% du PIB)"
    )

    return fig
