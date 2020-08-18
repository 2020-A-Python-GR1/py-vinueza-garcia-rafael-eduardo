# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:34 2020

@author: Rafael
"""

import pandas as pd

path_guardado = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#loc -> acceder a grupo de filas y columnas por LABEL
filtrado_horizontal = df.loc[1035] #Serie
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) #Indices son las columnas del dataframe

serie_vertical = df['artist']

print(serie_vertical)
print(serie_vertical.index) #Indices son los indices del dataframe

#Filtrado por indice
df_1035 = df[df.index == 1035]
segundo = df.loc[df.index == 1035] #Filtrar por arreglo True False   
segundo = df.loc[3:5] #rangos de valores
segundo = df.loc[1035, ['artist', 'medium']] #Varios indices    

#iloc - acceder a grupo de filas y columnas por indices en 0

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]
tercero = df.iloc[0:10, 0:4]

#################################################################

datos = {
    "nota 1":{
        "pepito":7,
        "Juanita":8,
        "Maria":9},
    "nota 2":{
        "pepito":7,
        "Juanita":8,
        "Maria":9},
    "disciplina":{
        "pepito":4,
        "Juanita":9,
        "Maria":2}
    }

notas = pd.DataFrame(datos)

condicion_nota1 = notas['nota 1'] <= 7
condicion_nota2 = notas['nota 1'] <= 7
condicion_disc = notas["disciplina"] <= 7

mayores_siete = notas.loc[condicion_nota1, ["nota 1"]]

pasaron = notas.loc[condicion_nota1][condicion_nota2][condicion_disc]

notas.loc["Maria","disciplina"] = 7

notas.loc[:,"disciplina"] = 7

################# Promedio de las 3 notas #################

promedio = (notas["nota 1"] + notas["nota 2"] + notas["disciplina"]) / 3

















