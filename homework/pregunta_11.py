"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_11():
    with open('./files/input/data.csv', newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        letras = [(letra, int(elemento[1])) for elemento in lectura for letra in elemento[3].split(',')]
        contador = {}
        for letra, valor in sorted(letras):
            if letra in contador:
                contador[letra] +=valor
            else: 
                contador[letra] = valor
        print(contador)
        return contador
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
pregunta_11()