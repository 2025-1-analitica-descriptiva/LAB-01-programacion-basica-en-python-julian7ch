"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
def pregunta_01():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        contador = 0
        for fila in lector:
            contador +=  int(fila[1])
        print(contador)
        return contador

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
pregunta_01()
