import plotly.express as px

def life_expectancy_developing_country_chart(data):
    if data is None:
        print("Les données sont introuvables pour créer le graphique.")
        return None
    developing = data[data['Status'] == "Developed"]
    
    # Créer le graphique
    fig = px.scatter(developing, 
                    x="Year", 
                    y="Life expectancy ", 
                    title="Life Expectancy Over Time",
                    hover_name="Country")
    return fig
