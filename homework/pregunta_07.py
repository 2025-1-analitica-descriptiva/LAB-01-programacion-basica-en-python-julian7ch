"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

import csv
def pregunta_07():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        listaInteres = [(elemento[1], elemento[0]) for elemento in lectura]
        diccionario = defaultdict(list)
        listaFinal = []

        for clave, letra in listaInteres:
            diccionario[clave].append(letra)

        for clave,valor in diccionario.items():
            listaFinal.append((int(clave),list(valor)))
        listaFinalOrdenada = sorted(listaFinal, key=lambda x: int(x[0])) 

        print(listaFinalOrdenada)
        return listaFinalOrdenada

    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 1 y una lista con todas las letras
    asociadas (columna 0) a dicho valor de la columna 1.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
pregunta_07()