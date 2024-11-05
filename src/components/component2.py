import plotly.express as px

def create_life_expectancy_chart(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    
    # Créer le graphique
    fig = px.line(data, x="Year", y="Life Expectancy ", title="Life Expectancy Over Time")
    return fig
