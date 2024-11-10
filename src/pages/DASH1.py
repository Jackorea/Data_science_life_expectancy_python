
import plotly.express as px
import plotly.io as pio
import dash
from dash import dcc, html
import webbrowser 

from src.utils.clean_data import load_cleaned_data
from src.components.component3 import life_expectancy_expenditure
from src.components.carte import carte
from src.components.component4 import life_expectancy_zimbabwe
from src.components.component import life_expectancy_percentage_expenditure_2010_paysdev
from src.components.component import life_expectancy_percentage_expenditure_2010_paysnodev
from src.components.component5 import life_thiness

def create_dashboard():
    app = dash.Dash(__name__)
    data = load_cleaned_data()
    if data is not None:

        fig = life_expectancy_expenditure(data)
        fig1 = life_expectancy_zimbabwe(data)
        fig2 = life_expectancy_percentage_expenditure_2010_paysdev(data)
        fig3 = life_expectancy_percentage_expenditure_2010_paysnodev(data)
        fig4 = life_thiness(data)
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
                html.P("Les données utilisées pour cette analyse proviennent de l'Organisation mondiale de la santé (OMS), garantissant des informations de haute qualité et fiables pour une interprétation raisonnée et correcte."),
                html.P("Nos données sont les suivantes :"),
                html.Ul([
                html.Li("Pays du monde : country"),
                html.Li("Années des données de 2000 à 2015 : Year"),
                html.Li("Status : Status (Développé ou en Développement)"),
                html.Li("Espérance de vie : Life expectancy (en âge)"),
                html.Li("Mortalité des adultes : Adult Mortality (probabilité de mourir entre 15 et 60 ans pour 1000 personnes)"),
                html.Li("Mortalité infantile : infant deaths (nombre de décès d'enfants pour 1000 naissances)"),
                html.Li("Taux d'alcool : Alcohol (consommation par habitant (15+) en litres d'alcool pur)"),
                html.Li("Pourcentage de dépense d'état dans le PIB : percentage expenditure (dépenses de santé en % du PIB par habitant)"),
                html.Li("Hépatite B : Hepatitis B (couverture vaccinale des enfants de 1 an en %)"),
                html.Li("Rougeoles : Measles (nombre de cas rapportés pour 1000 habitants)"),
                html.Li("Indice de masse corporelle : BMI (IMC moyen de la population)"),
                html.Li("Mortalité des enfants de moins de 5 ans : Under-five deaths (pour 1000 habitants)"),
                html.Li("Polio : Polio (couverture vaccinale des enfants de 1 an en %)"),
                html.Li("Dépenses de santé (% des dépenses gouvernementales totales) : Total expenditure"),
                html.Li("Diphtérie : Diphtheria (couverture de vaccination DTP3 des enfants de 1 an en %)"),
                html.Li("Taux de sida et VIH : HIV/AIDS (décès pour 1000 naissances vivantes chez les 0-4 ans)"),
                html.Li("Produit Intérieur Brut (PIB) : GDP (en USD)"),
                html.Li("Minceur chez les 10-19 ans : thinness prevalence (pourcentage)"),
                html.Li("Minceur chez les 5-9 ans : thinness prevalence (pourcentage)"),
                html.Li("Indice de ressources : Income composition of resources (Indice de développement humain de 0 à 1)"),
                html.Li("Années de scolarité : Schooling (nombre d'années de scolarité)")
            ])
            ])
        ]),
        
        # Onglet Graphique
        dcc.Tab(label='L etat doit il investir de l argent dans la santé  ', children=[
            html.Div([
                dcc.Graph(
                    id='graph1',
                    figure=fig if fig is not None else {},  # On vérifie que `fig` est non-nul
                    config={'displayModeBar': False}
                ),
                html.Div(children=f'''
                    L'histogram ci-dessus montre la relation entre l'espérance de vie et les dépenses
                    de santé pour l'année 2008. Les barres indiquent la répartition des pays, on remarque que l'espérence de vie est
                    le plus élevée pour les pays investissant le plus. On peut donc penser que plus les pays investissant dans la santé 
                    plus l'espérence de vie diminuera. Egalement, ici on prend le pourcentage en compte des dépenses de santé en fonction des dépenses 
                    totales. 
                ''')
            ])
        ]),
        
        # Onglet Carte VIH
        dcc.Tab(label='Carte VIH et graphique evolution', children=[
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
                    On remarque ici par la fin de l'animation que dans les pays ou le taux de sida est le plus élevé, la baisse de ce taux 
                         a entrainé une importante hausse de l'espérence de vie. C'est donc un facteur très important. 
                ''')
            ])
        ]),
        # Onglet Vaccination
        dcc.Tab(label=' Impact de la Vaccination ici diphteria ', children=[
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
                    On remarque que tout les pays dévelopées ont une espérence de vie de plus de 72 ans et une campagne de vaccination 
                    efficace tandis que pour les pays en développement certaines campagnes sont moins présente et du coup
                    baisse l'espérence de vie
                ''')
            ])
        ]),
        # Onglet Thiness
        dcc.Tab(label='Impact de la minceur des 5/19 ans ', children=[
                html.Div([
                dcc.Graph(
                    id='graph5',
                    figure=fig4 if fig4 is not None else {},
                    config={'displayModeBar': False}
                ),
                html.Div(children='''
                    La valeur de 5 est atteinte seulement par les pays en développement, on remarque la plus de la moitié des pays en développement 
                    sont victime de minceur et donc elle a un impact sur l'espérence de vie. 
                    
                ''')
            ])
        ]),
    ])
])

    webbrowser.open("http://127.0.0.1:8050/")
    app.run_server(debug=True, use_reloader =False)
    
if  __name__ == '__main__':
    create_dashboard()
