"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_10():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        listaInteres = [(elemento[0],len(elemento[3].split(',')),len(elemento[4].split(','))) for elemento in lectura]
        print(listaInteres)
        return listaInteres
        
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
pregunta_10()