import pandas as pd
import folium
import requests, json
import urllib.parse

def carte(data):
    world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='OpenStreetMap')
    for index, row in data.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5 + row['Prevalence'] * 2,  # Ajuster la taille du cercle en fonction de la prévalence
          color='crimson',
            fill=True,
            fill_color='crimson',
            fill_opacity=0.6,
            popup=f"{row['Country']}: {row['Prevalence']}%"
        ).add_to(world_map)
    world_map.save("vih_prevalence_map.html")

