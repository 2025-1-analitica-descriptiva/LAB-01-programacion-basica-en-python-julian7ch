"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from collections import defaultdict


def pregunta_09():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        listaInteres = [elemento[4].split(',') for elemento in lectura]
        listaSeparada = [tuple(elemento.split(':'))[0] for items in listaInteres for elemento in items]
        contador = {}

        for i in sorted(listaSeparada):
            if i in contador:
                contador[i] += 1
            else:
                contador[i] = 1

        print(contador)  
        return contador

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
pregunta_09()