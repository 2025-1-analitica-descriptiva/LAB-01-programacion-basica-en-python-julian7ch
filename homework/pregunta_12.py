"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_12():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        listaInteres = [(elemento[0],int(numeros.split(':')[1])) for elemento in lectura for numeros in elemento[4].split(',')]
        contador = {}

        for letra,valor in sorted(listaInteres):
            if letra in contador:
                contador[letra] += valor
            else:
                contador[letra] = valor
        print(contador)
        return contador
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
pregunta_12()