
import plotly.express as px
import plotly.io as pio
import dash
from dash import dcc, html
import webbrowser 

from src.utils.get_data import load_cleaned_data
from src.components.component3 import life_expectancy_expenditure
from src.components.carte import carte
from src.components.component4 import life_expectancy_zimbabwe
from src.components.component import life_expectancy_percentage_expenditure_2010_paysdev
from src.components.component import life_expectancy_percentage_expenditure_2010_paysnodev

def create_dashboard():
    app = dash.Dash(__name__)
    data = load_cleaned_data()
    if data is not None:

        fig = life_expectancy_expenditure(data)
        fig1 = life_expectancy_zimbabwe(data)
        fig2 = life_expectancy_percentage_expenditure_2010_paysdev(data)
        fig3 = life_expectancy_percentage_expenditure_2010_paysnodev(data)
        car = carte(data)  # Génère le fichier `vih_prevalence_map.html`
    else:
        fig = None
        print("Erreur lors du chargement des données.")


    app.layout = html.Div(children=[
        html.H1("Dashboard : L'importance de la santé dans le monde"),
        dcc.Tabs([
        # Onglet Présentation du projet
        dcc.Tab(label='Présentation du projet', children=[
            html.Div([
                html.H2("Présentation du projet"),
                html.P('''
                    Quelles sont les éléments qui impact le plus l'espérence de vie d'une population?
                       

                    
                    Ce dashboard présente une analyse de divers facteurs ayant un impact
                    sur l'espérance de vie, tels que le taux du VIH en pourcentage de la population, les dépenses
                    de santé, et l'importance de la vaccination. L'objectif est de fournir 
                    des renseignements sur les relations entre ces éléments et les résultats de santé 
                    dans différents pays pour connaitre l'impact de ses éléments sur l'espérence de vie .
                '''),
                html.P('''
                    
                       
                    Les données utilisées pour cette analyse proviennent de l'Organisation
                    mondiale de la santé (OMS), garantissant des informations de haute qualité
                    et fiable pour une interprétation raisonnée et correct.
                    
                    Nos données sont les suivantes: 
                    Les pays du monde: country
                    Les années des données de 2000 à 2015:Year
                    Le Status: Status (Developed or Developing). 
                    L'espérence de vie: Life expectancy( en age)
                    La motalité des adultes:  Adult Mortality (probability of dying between 15 and 60 years per 1000 population)
                    La mortalité infantile: infant deaths (Number of Infant Deaths per 1000 population) 
                    Le taux d'alcool: Alcohol (recorded per capita (15+) consumption (in litres of pure alcohol))
                    Le pourcentage de depense d'etat PIB: percentage expenditure(Expenditure on health as a percentage of Gross Domestic Product per capita(%))
                    Hepatide B: Hepatitis B  immunization coverage among 1-year-olds (%). 
                    Rougeoles: Measles - number of reported cases per 1000 population. 
                    Indice masse corporelle: BMI Average Body Mass Index of entire population
                    Mort enfent 5 nas under-five deaths (per 1000 population)
                    Polio: Polio (immunization coverage among 1-year-olds (%))
                    Dépense en santé selon toute les dépenses: Total expenditure (General government expenditure on health as a percentage of total government expenditure (%))
                    Diphtheria: Diphtheria (tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%))
                    Taux de sida et vih: HIV/AIDS (Deaths per 1 000 live births HIV/AIDS (0-4 years))
                    PIB: GDP  (in USD)
                    Population 
                    Minceur: thinness 1-19 years: Prevalence of thinness among children and adolescents for Age 10 to 19 (% )
                    Minceur: thinness 5-9 years: Prevalence of thinness among children for Age 5 to 9(%)
                    Resoouce: Income composition of resources(Human Development Index (index ranging from 0 to 1)
                    Année à l'école: Schooling Number of years of Schooling(years)
                ''')
            ])
        ]),
        
        # Onglet Graphique
        dcc.Tab(label='Graphique', children=[
            html.Div([
                dcc.Graph(
                    id='graph1',
                    figure=fig if fig is not None else {},  # On vérifie que `fig` est non-nul
                    config={'displayModeBar': False}
                ),
                html.Div(children=f'''
                    L'histogram ci-dessus montre la relation entre l'espérance de vie et les dépenses
                    de santé pour l'année 2008. Chaque point représente un pays avec ses propres
                    valeurs de dépenses et d'espérance de vie. 
                ''')
            ])
        ]),
        
        # Onglet Carte VIH
        dcc.Tab(label='Carte VIH', children=[
            html.Div([
                html.P('''
                    Cette page nous permet de renseigner l'impact de la campagne de lutte contre le vih et le sida
                       qui a permis de sauver de nombreuses personnes et d'augmenter l'espérence de vie dans ses pays. 
                '''),
                html.H2("Carte de la prévalence du VIH"),
                html.Iframe(srcDoc=car, width="100%", height="500px"),
                # Onglet Graphique avec animation
                dcc.Graph(
                    id='graph2',
                    figure=fig1 if fig1 is not None else {},
                    config={'displayModeBar': False}
                ),
                html.Div(children='''
                    Le graphique ci-dessus montre l'évolution de l'espérance de vie par rapport au taux de VIH au fil des années.
                ''')
            ])
        ]),
        # Onglet BMI 
        dcc.Tab(label='Graphique', children=[
                html.Div([
                dcc.Graph(
                    id='graph3',
                    figure=fig2 if fig2 is not None else {},
                    config={'displayModeBar': False}
                ),
                dcc.Graph(
                    id='graph4',
                    figure=fig3 if fig3 is not None else {},
                    config={'displayModeBar': False}
                ),
                html.Div(children='''
                    on regarde les pays dévelopés 
                ''')
            ])
        ]),
    ])
])

    webbrowser.open("http://127.0.0.1:8050/")
    app.run_server(debug=True, use_reloader =False)
    
if  __name__ == '__main__':
    create_dashboard()
