"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_02():
    with open('./files/input/data.csv', newline='', encoding= 'utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter = '\t')
        lista = []
        contador = {}

        for elemento in lectura:
            lista.append(elemento[0])


        for letra in lista:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
        
    
        conteoLetras = sorted(list(contador.items()))
        
        print(lista)
        print(conteoLetras)

        return conteoLetras
        
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
pregunta_02()