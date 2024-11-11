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
    fig = px.histogram(
        year2008,
        x='Life expectancy ',
        y='Total expenditure',
        nbins=10, 
        title='Histogramme de l\'espérance de vie et des dépenses de santé en 2008',
        labels={'Life expectancy ': 'Espérance de vie', 'Total expenditure ': 'Dépense des dépenses des pays selon leur dépenses totales'},
        color_discrete_sequence=['#636EFA']
    )
    
    fig.update_layout(
        xaxis_title="Espérance de vie",
        yaxis_title="Total expenditure"
    )

    return fig

