import plotly.express as px

def life_thiness(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    year2008 = data[data['Year'] == 2008]
    # Créer le graphique
    fig = px.scatter(year2008, 
                    x="Life expectancy ", 
                    y=" thinness  1-19 years", 
                    title="L espérance de vie en fonction de la minceur",
                    hover_name="Country", color="Status")
    return fig
def infant_deaths_thiness(data):
    year2008 = data[data['Year'] == 2008]
    # Créer le graphique
    fig = px.scatter(year2008, 
                    x="infant deaths", 
                    y=" thinness  1-19 years", 
                    title="La mortalité infantile en fonction de la minceur",
                    hover_name="Country", color="Status")
    return fig
