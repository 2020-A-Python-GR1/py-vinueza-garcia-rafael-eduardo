# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:46:54 2020

@author: Rafael
"""
#c_dataframes.py

import numpy as np
import pandas as pd

arr_pandas = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pandas)

s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

df1[3] = s1
df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
        arr_pandas,
        columns = [
            'Estatura (cm)',
            'Peso (Kg)',
            'Edad (anios)'])

datos_fisicos_dos = pd.DataFrame(
        arr_pandas,
        columns = [
            'Estatura (cm)',
            'Peso (Kg)',
            'Edad (anios)'],
        index = [
            'Rafael',
            'Eduardo'])

serie_peso = datos_fisicos_dos['Peso (Kg)']
datos_rafael = serie_peso['Rafael']
print(serie_peso)
print('\n')
print(datos_rafael)

df1.index = ['Rafael', 'Eduardo']
df1.columns = ['A','B','C','D','E']











