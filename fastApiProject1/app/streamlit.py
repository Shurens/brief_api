import streamlit as st
import pandas as pd
import requests
import folium
import requests
from streamlit_folium import folium_static
from folium.plugins import HeatMap


# la connection avec l'API
API_URL = "http://api:8002"

# Faire une requête GET à l'API pour obtenir les données de la base de données
response = requests.get(f"{API_URL}/all_species")
data = response.json()

# Créer un DataFrame à partir des données
df = pd.DataFrame(data)

# Filtrer les années uniques en excluant les valeurs vides (NaN)
annees_uniques = df['Start_Year'].dropna().unique()

# Tri des animaux uniques par ordre alphabétique
animaux_uniques = df['Common_name'].unique()

# Widget selectbox pour permettre à l'utilisateur de choisir l'animal
animal_selection = st.selectbox("Sélectionnez un animal :", animaux_uniques)

# Afficher les informations de la première ligne trouvée pour l'animal sélectionné
animal_info = df[df['Common_name'] == animal_selection].iloc[0]
st.subheader("Informations sur l'animal sélectionné :")
st.write(f"Nom commun : {animal_info['Common_name']}")
st.write(f"Nom scientifique : {animal_info['Scientific_name']}")
st.write(f"Identifiant : {animal_info['Species_ID']}")
st.write(f"Ordre : {animal_info['Order']}")
st.write(f"Famille : {animal_info['Family']}")
st.write(f"Genre : {animal_info['Genus']}")

# Widget selectbox pour permettre à l'utilisateur de choisir une année
annee_selection = st.selectbox("Sélectionnez une année :", annees_uniques)

# Filtrer les données en fonction de l'animal sélectionné
df_animal = df[df['Common_name'] == animal_selection]

# Filtrer les données en fonction de l'année sélectionnée
df_animal_annee = df_animal[df_animal['Start_Year'] == annee_selection]

if not df_animal_annee.empty:
    map_center = [df_animal_annee.iloc[0]['Latitude'], df_animal_annee.iloc[0]['Longitude']]
    m = folium.Map(location=map_center, zoom_start=6)

    # Créer une liste de coordonnées pour la heatmap
    heatmap_data = df_animal_annee[['Latitude', 'Longitude']].values.tolist()

    # Créer la heatmap et l'ajouter à la carte
    HeatMap(heatmap_data).add_to(m)

    # Afficher la carte
    st.subheader(f'Carte des observations de l\'animal : {animal_selection} pour l\'année {annee_selection}')
    folium_static(m)
else:
    st.warning("Aucune observation trouvée pour l'année sélectionnée.")