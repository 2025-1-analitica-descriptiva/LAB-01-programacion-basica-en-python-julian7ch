"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

import csv

def pregunta_05():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        listaEspecial = [(elemento[0], int(elemento[1])) for elemento in lectura] 
        nuevaLista = defaultdict(list)
        resultado = []
        for letra,numero in sorted(listaEspecial):
            nuevaLista[letra].append(numero)

        for letra,numeros in nuevaLista.items():
            maxNumero = max(numeros)
            minNumero = min(numeros)
            resultado.append((letra, maxNumero, minNumero))
        print(resultado)
        return resultado

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
pregunta_05()