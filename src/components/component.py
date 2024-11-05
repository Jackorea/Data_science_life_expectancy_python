import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
life = pd.read_csv("Updated_Life_Expectancy_Data.csv")
print(life)
#print(life.head())
print(life.describe())
Countries = life["Country"]
Countries = Countries.unique()
print(Countries)
Years = life["Year"]
Years = Years.unique()
print(Years)
status= life["Status"]
status=status.unique()
print(status)




Year = 2010
Status = 'Developing'
yearDeveloping = life.query("Year==2010 and Status=='Developing'")
print(yearDeveloping)



trace = go.Scatter( x=yearDeveloping['Life expectancy '],
                    y=yearDeveloping[' BMI '],
                     mode='markers',
                    text=yearDeveloping['Country'],      
                    hoverinfo='text+x+y' )
data = [trace] 
layout = go.Layout( title="fgvhbjnk,",
                    xaxis= dict(title="Life expect"),
                    yaxis=dict(title="Alcohol Consumption"), )
fig = go.Figure(data=data, layout=layout)
plotly.io.write_html(fig, file='fig.html', auto_open=True, include_plotlyjs='cdn')

