# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:28:44 2020

@author: Rafael
"""
import numpy as np
import pandas as pd
import os
import sqlite3
import xlsxwriter

path_guardado = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# Tipos de archivos
#JSON, Excel, SQL

path_excel = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.xlsx"

#Con el indice como columna
sub_df.to_excel(path_excel)

# Sin el indice como columna
sub_df.to_excel(path_excel, index = False)


columnas = ['artist','title','year']
sub_df.to_excel(path_excel, columns = columnas)

path_excel_mt = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data_mt.xlsx"
writer = pd.ExcelWriter(path_excel_mt, engine = 'xlsxwriter')
sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')
writer.save()

#Formato Condicional

path_excel_colores = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data_colores.xlsx"
writer = pd.ExcelWriter(path_excel_colores, engine = 'xlsxwriter')
num_artistas = sub_df['artist'].value_counts()
num_artistas.to_excel(writer, sheet_name = 'Artistas')
hoja_artistas = writer.sheets['Artistas']
ultimo_numero = len(num_artistas.index) + 1
rango_celdas = f'B2:B{ultimo_numero}'

formato_artistas = {
    "type": "2_color_scale",
    "min_value":10,
    "min_type":"percentile",
    "max_value":99,
    "max_type":"percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)
writer.save()

#DEBER 03 - Grafico de artistas

artistas = num_artistas.index

workbook = xlsxwriter.Workbook('data//artwork_data_grafico.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Artista')
worksheet.write('B1', 'Obras')

for i in range(num_artistas.size):
    worksheet.write(f'A{i + 2}', artistas[i])
    worksheet.write(f'B{i + 2}', num_artistas[artistas[i]])

chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'name': 'Artistas y su numero de obras',
    'categories': f'=Sheet1!$A$2:$A${ultimo_numero}',
    'values':     f'=Sheet1!$B$2:$B${ultimo_numero}'
})

worksheet.insert_chart('D3', chart)

workbook.close()

############## SQL #######################

#with sqlite3.connect("bdd_artist.bdd") as conexion:
#    sub_df.to_sql('py_artistas', conexion)
    
## with mysql.connect('mysql://user:password@ip:puerto/nombre_base')
##      df5.to_sql('tabla_mysql', conexion)

############## JSON #######################

#sub_df.to_json('artistas.json')
#sub_df.to_json('artistas_tabla.json', orient = 'table')



