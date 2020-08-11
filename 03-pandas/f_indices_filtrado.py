# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:48 2020

@author: Rafael
"""

import pandas as pd

path_guardado = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)
print(type(artistas)) #numpy array
print(artistas.size)

blake = df['artist'] == 'Blake, William' #Serie
print(blake.value_counts())
df_blake = df[blake] #Dataframe