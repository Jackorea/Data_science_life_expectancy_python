import plotly.express as px
import pandas as pd

def life_expectancy_zimbabwe(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    countries = data[data['Country'].isin(["Zimbabwe", "France", "Swaziland", "Botswana", "Kenya"])]
    countries = countries.sort_values(by="Year")
    fig = px.scatter(
        countries,
        x="Life expectancy ", y=" HIV/AIDS", animation_frame="Year",color="Country", size=" HIV/AIDS", 
        hover_name="Country", labels={'HIV/AIDS': 'Taux de VIH (%)', 'Life expectancy ': 'Espérance de vie'},
        color_discrete_sequence=px.colors.qualitative.Safe, title="Évolution de l'espérance de vie en fonction du taux de VIH"
    )
    
    fig.update_layout(
        xaxis_title="Espérence de vie ",
        yaxis_title="Taux de vih dans leur population "
    )

    return fig