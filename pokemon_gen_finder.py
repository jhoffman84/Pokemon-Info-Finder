import streamlit as st
import requests
import pandas as pd

#Title

def title():
    st.header("Pokemon Info Finder")
    st.image("International_Pokémon_logo.png")
    st.write("Input your Generation of Pokemon in here and we will find what pokemon appeared for the first time in your Generation!")

title()

generation = str(st.number_input("Generation", min_value=1, value=1, max_value=8)) #New 1



# Api Loader
def api(generation):
    baselink= "https://pokeapi.co/api/v2/generation/"
    r= requests.get(baselink+generation)
    data=r.json()
    number_of_pokemon = len(data["pokemon_species"])
    st.subheader(f"In Generation {generation}, there were {number_of_pokemon} different pokemon species introduced!")
    alist=[]
    for pokemon in data["pokemon_species"]:
        alist.append((f"{pokemon['name']}"))
        games = data['version_groups'][0]['name'].split('-')
    st.subheader(f"You generation is from the Games Pokemon {games[0]} & {games[1]}")
    st.write(f"Here is the Full List of all pokemon introduced in Generation {generation}!")
    st.write(alist)
    st.write("For more info on a Pokemon input put it's index here:")
    number = st.slider("Pokemon Index",min_value=0, max_value=len(data['pokemon_species'])) #New 2
    st.write(f"You've selected {data['pokemon_species'][number]['name']}")
    st.image(f"https://img.pokemondb.net/artwork/avif/{data['pokemon_species'][number]['name']}.avif")
    r = requests.get(data['pokemon_species'][number]["url"])
    data2=r.json()
    toggle=st.toggle("Show Info", value=False) # New 3
    if toggle:
        for key,item in data2.items():
            key=key.split('_')
            real_key=""
            for word in key:
                real_key += word[0].upper() + word[1:] + ' '
            real_key = real_key[0:len(real_key)-1]
            expander = st.expander(f"{real_key}")
            expander.write(item)


api(generation)

