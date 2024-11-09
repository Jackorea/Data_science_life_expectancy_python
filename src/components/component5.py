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
                    title="Life Expectancy Over Time",
                    hover_name="Status", color="Status")
    return fig
