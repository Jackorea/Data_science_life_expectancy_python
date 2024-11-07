
import plotly.express as px
import plotly.io as pio
import dash
from dash import dcc, html

from src.utils.get_data import load_cleaned_data
from src.components.component3 import life_expectancy_expenditure
from src.components.carte import carte


def create_dashboard():
    app = dash.Dash(__name__)
    data = load_cleaned_data()
    if data is not None:

        fig = life_expectancy_expenditure(data)
        #carte(data)  # Génère le fichier `vih_prevalence_map.html`
    else:
        fig = None
        print("Erreur lors du chargement des données.")


    app.layout = html.Div(children=[
        html.H1("Dashboard : Espérance de vie et dépenses de santé"),

    # Afficher le graphique
    dcc.Graph(
        id='graph1',
        figure=fig if fig is not None else {},  # On vérifie que `fig` est non-nul
        config={'displayModeBar': False}
    ),
    
    # Description
    html.Div(children=f'''
        Le graphique ci-dessus montre la relation entre l'espérance de vie et les dépenses
        de santé pour l'année 2008. Chaque point représente un pays avec ses propres
        valeurs de dépenses et d'espérance de vie. La carte montre la prévalence du VIH
        par pays.
    ''')
    ])
    app.run_server(debug=True)
    
    
if  __name__ == '__main__':
    create_dashboard()