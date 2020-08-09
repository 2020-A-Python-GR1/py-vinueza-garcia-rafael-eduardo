# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:09:24 2020

@author: Rafael
"""

#DEBER 3 - Grafico de artistas en excel con xlsxwriter

import numpy as np
import pandas as pd
import os
import xlsxwriter

path_guardado = "C://Users//Equipo//Documents//Gitkraken//py-vinueza-garcia-rafael-eduardo//03-pandas//data//artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

num_artistas = sub_df['artist'].value_counts()

ultimo_numero = len(num_artistas.index) + 1

artistas = num_artistas.index

workbook = xlsxwriter.Workbook('artwork_data_grafico.xlsx')
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