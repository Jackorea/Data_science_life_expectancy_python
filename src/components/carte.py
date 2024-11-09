import pandas as pd
import folium
import requests, json
import urllib.parse
from geopy.geocoders import Nominatim
import pandas as pd
import folium
import json
import time 
def carte(data):
    year2004 = data[data['Year'] == 2004]
    countries = year2004['Country'].unique()
    geolocator = Nominatim(user_agent="myVihPrevalenceApp_2024")
    coordinates = {}
    for c in countries:
        location = geolocator.geocode(c)
        if location:
            coordinates[c] = (location.latitude, location.longitude)
        else:
            coordinates[c] = (None, None) 
        time.sleep(0.1)  
    
    world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='OpenStreetMap')
    for index, row in data.iterrows():
        country = row['Country']
        vih = row[' HIV/AIDS']
        if country in coordinates and None not in coordinates[country]:
            lat, lon = coordinates[country]
            folium.CircleMarker(
                location=[lat, lon],
                radius= 0.8+ vih * 0.7,  # Ajuster la taille du cercle en fonction de la prévalence
                color='crimson',
                fill=True,
                fill_color='crimson',
                fill_opacity=0.4,
                popup=f"{country}: {vih}%"
            ).add_to(world_map)

    # Sauvegarder la carte dans un fichier HTML
    #world_map.save("vih_prevalence_map_2004.html")
    return world_map._repr_html_()