import pandas as pd
import folium
import requests, json
import urllib.parse
from geopy.geocoders import Nominatim
import pandas as pd
import folium
import json

# Charger le fichier GeoJSON des pays
with open('countries.geo.json') as f:
    countries_geojson = json.load(f)
def carte(data):
    # Créer la carte centrée sur le monde
    world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='OpenStreetMap')

    # Ajouter les pays sur la carte avec les informations du GeoJSON
    folium.GeoJson(countries_geojson).add_to(world_map)

    # Ajouter les cercles pour la prévalence du VIH
    year2004 = data[data['Year'] == 2004]
    for index, row in year2004.iterrows():
        country = row['Country']
        vih = row[' HIV/AIDS']
        
        # Utiliser un géocodage simple ou un nom de pays pour obtenir la position
        # Ici, nous utilisons un dictionnaire manuel (à compléter avec des coordonnées)
        coordinates = get_country_coordinates(country)  # Crée ta propre méthode pour obtenir les coordonnées
        if coordinates:
            lat, lon = coordinates
            folium.CircleMarker(
                location=[lat, lon],
                radius=5 + vih * 2,  # Ajuste la taille du cercle en fonction de la prévalence
                color='crimson',
                fill=True,
                fill_color='crimson',
                fill_opacity=0.6,
                popup=f"{country}: {vih}%"
            ).add_to(world_map)

    # Sauvegarder la carte dans un fichier HTML
    world_map.save("vih_prevalence_map_2004.html")
"""
def carte(data):
    year2004 = data[data['Year'] == 2004]
    countries = year2004['Country'].unique()
    geolocator = Nominatim(user_agent="myGeocoder")
    coordinates = {}
    for c in countries:
        location = geolocator.geocode(c)
        if location:
            coordinates[c] = (location.latitude, location.longitude)
        else:
            coordinates[c] = (None, None) 
        time.sleep(1)  
    
    world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='OpenStreetMap')
    for index, row in data.iterrows():
        country = row['Country']
        vih = row[' HIV/AIDS']
        if country in coordinates and None not in coordinates[country]:
            lat, lon = coordinates[country]
            folium.CircleMarker(
                location=[lat, lon],
                radius=5 + vih * 2,  # Ajuster la taille du cercle en fonction de la prévalence
                color='crimson',
                fill=True,
                fill_color='crimson',
                fill_opacity=0.6,
                popup=f"{country}: {vih}%"
            ).add_to(world_map)

    # Sauvegarder la carte dans un fichier HTML
    world_map.save("vih_prevalence_map_2004.html")
"""