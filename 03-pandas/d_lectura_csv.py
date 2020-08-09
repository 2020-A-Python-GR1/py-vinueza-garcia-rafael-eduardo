# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:52 2020

@author: Rafael
"""

path = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ['id','artist','title','medium','year','acquisitionYear','height','width','units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')

path_guardado = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)