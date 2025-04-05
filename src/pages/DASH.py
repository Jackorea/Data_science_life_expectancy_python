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
from src.components.component5 import infant_deaths_thiness
from src.components.component3 import histo
from src.components.component3 import histo2
def create_dashboard():
    app = dash.Dash(__name__)
    data = load_cleaned_data()
    if data is not None:

        fig = life_expectancy_expenditure(data)
        fig1 = life_expectancy_zimbabwe(data)
        fig2 = life_expectancy_percentage_expenditure_2010_paysdev(data)
        fig3 = life_expectancy_percentage_expenditure_2010_paysnodev(data)
        fig4 = life_thiness(data)
        fig5 = histo(data)
        fig6 = histo2(data)
        fig7 = infant_deaths_thiness(data)
        car = carte(data)  # Génère le fichier `vih_prevalence_map.html`
    else:
        fig = None
        print("Erreur lors du chargement des données.")


    app.layout = html.Div(children=[
    html.H1("Dashboard : Quelles facteurs influencent notre espérance de vie"),
    dcc.Tabs([
        # Onglet Présentation du projet
        dcc.Tab(label='Présentation du projet', children=[
            html.Div([
                html.H2("Présentation du projet"),
                html.P('''
                    Quelles sont les éléments qui impactent le plus l'espérance de vie d'une population?
                       

                    
                    Ce dashboard présente une analyse de divers facteurs ayant un impact
                    sur l'espérance de vie, tels que le taux du VIH en pourcentage de la population, les dépenses
                    de santé, et l'importance de la vaccination. L'objectif est de fournir 
                    des renseignements sur les relations entre ces éléments et les résultats de santé 
                    dans différents pays pour connaître l'impact de ces éléments sur l'espérance de vie .
                '''),
                html.P("Les données utilisées pour cette analyse proviennent de l'Organisation mondiale de la santé (OMS), garantissant des informations de haute qualité et fiables pour une interprétation raisonnée et correcte."),
                html.P("Nos données sont les suivantes :"),
                html.Ul([
                html.Li("Pays du monde : country"),
                html.Li("Années des données de 2000 à 2015 : Year"),
                html.Li("Statut : Status (Développé ou en Développement)"),
                html.Li("Espérance de vie : Life expectancy (en âge)"),
                html.Li("Mortalité des adultes : Adult Mortality (probabilité de mourir entre 15 et 60 ans pour 1000 habitants)"),
                html.Li("Mortalité infantile : infant deaths (nombre de décès d'enfants pour 1000 naissances)"),
                html.Li("Taux d'alcool : Alcohol (consommation par habitant (15+) en litres d'alcool pur)"),
                html.Li("Pourcentage de dépense d'état dans le PIB : percentage expenditure (dépenses de santé en % du PIB par habitant)"),
                html.Li("Hépatite B : Hepatitis B (couverture vaccinale des enfants de 1 an en %)"),
                html.Li("Rougeoles : Measles (nombre de cas rapportés pour 1000 habitants)"),
                html.Li("Indice de masse corporelle : BMI (IMC moyen de la population)"),
                html.Li("Mortalité des enfants de moins de 5 ans : Under-five deaths (pour 1000 habitants)"),
                html.Li("Polio : Polio (couverture vaccinale des enfants de 1 an en %)"),
                html.Li("Dépenses de santé : Total expenditure (% des dépenses gouvernementales totales) "),
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
        dcc.Tab(label='Investissement dans la santé', children=[
            html.Div([
                html.Div(children=f'''
                    Pour commencer nous allons créer un histogramme de l'espérance de vie en fonction de leur fréquence.
                    On le fera à deux périodes différentes pour pouvoir voir l'évolution de l'espérence de vie 
                    selon les pays.
                '''),
                dcc.Graph(
                    id='graph11',
                    figure=fig5 if fig5 is not None else {},  
                    config={'displayModeBar': False}
                ),
                dcc.Graph(
                    id='graph12',
                    figure=fig6 if fig6 is not None else {},  
                    config={'displayModeBar': False}
                ),
                html.Div(children=f'''
                    Comme nous pouvons voir le résultat est encourageant puisque l'espérance de vie 
                         est moins importante au départ. Dans la suite de ce dashboard nous trouverons des raisons. 
                         Une première envisagée est de regarder si les pays qui investissent le plus dans la santé 
                         , on une espérance de vie plus élevé. 
                '''),
                dcc.Graph(
                    id='graph13',
                    figure=fig if fig is not None else {},  
                    config={'displayModeBar': False}
                ),
                html.Div(children=f'''
                    Le graphique ci-dessus est un nuage de points (scatter plot) qui montre la relation 
                    entre l'espérance de vie et les dépenses de santé pour l'année 2008. Chaque point représente un pays. 
                    On observe que les pays qui investissent davantage dans la santé ont généralement une espérance de vie plus élevée. 
                    Cela suggère une corrélation positive entre les dépenses de santé (en pourcentage des dépenses totales) et l'espérance de vie.
                ''')
            ])
        ]),
        
        # Onglet Carte VIH
        dcc.Tab(label='Carte VIH et graphique evolution', children=[
            html.Div([
                html.P('''
                    Cette onglet permet d'étudier l'impact de la campagne de lutte contre le vih et du sida. 
                '''),
                html.H2("Carte de la prévalence du VIH"),
                html.Iframe(srcDoc=car, width="100%", height="500px"),
                html.Div(children='''
                    Nous remarquons que la valeur en Afrique est très élevée pour les pays du Sud. Nous décidons 
                    alors de regarder dans le temps si une baisse du vih entrainera une augmentation de l'espérence de
                    vie pour ses pays. 
                '''),
                # Graphique avec animation
                dcc.Graph(
                    id='graph2',
                    figure=fig1 if fig1 is not None else {},
                    config={'displayModeBar': False}
                ),
                html.Div(children='''
                    Le graphique ci-dessus montre l'évolution de l'espérance de vie par rapport au taux de VIH au fil des années.
                    On remarque ici par la fin de l'animation que dans les pays où le taux de sida est le plus élevé, la baisse de ce taux 
                         a entraîné une importante hausse de l'espérence de vie. Notre hypothéses est validé et nous pouvons affirmer 
                         que le vih est un facteur très important à prendre en compte dans l'espérence de vie. 
                ''')
            ])
        ]),
        # Onglet Vaccination
        dcc.Tab(label=' Impact de la Vaccination ici polio', children=[
                html.Div([
                html.Div(children='''
                    Dans cette partie nous souhaitons découvrir si la vaccination a un impact, s'il est intelligent 
                         que des états investissent dans des campagnes de vaccination. 
                '''),
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
                    On remarque que tout les pays développés ont une espérance de vie de plus de 72 ans et une campagne de vaccination 
                    efficace de près de 100% tandis que c'est plus variable pour les pays en développement même si on remarque 
                    que plusieurs groupes de points se forment. En effet, on remarque qu'un grand groupe de pays qui on une espérance 
                    de vie de plus de 70 ans ont une campagne vaccinale élevée.  On remarque également un groupe de pays avec une campagne
                         vaccinale faible, leur espérence de vie est inférieur à 70. Pour les autres pays avec une campagne modérée
                    nous pouvons penser que d'autres facteurs peuvent causés une mauvaise espérance de vie.  
                ''')
            ])
        ]),
        # Onglet Thiness
        dcc.Tab(label='Impact de la minceur des 5/19 ans ', children=[
                html.Div([
                html.Div(children='''
                    La dernière partie de ce dashboard parle de l'impact possible de la minceur des enfants sur l'espérence 
                         de vie. 
                    
                '''),
                dcc.Graph(
                    id='graph5',
                    figure=fig4 if fig4 is not None else {},
                    config={'displayModeBar': False}
                ),
                html.Div(children='''
                    La valeur de 5 est atteinte seulement par les pays en développement, cette valeur est atteinte par au moins
                         la moitié de ces pays. La plupart des pays qui sont victimes de minceurs ont une espérance de vie
                         et donc elle a un impact sur l'espérance de vie. 
                    
                '''),
                dcc.Graph(
                    id='graph23',
                    figure=fig7 if fig7 is not None else {},
                    config={'displayModeBar': False}
                )
            ])
        ]),
    ])
])

    webbrowser.open("http://127.0.0.1:8050/")
    app.run_server(debug=True, use_reloader =False)
    
if  __name__ == '__main__':
    create_dashboard()
