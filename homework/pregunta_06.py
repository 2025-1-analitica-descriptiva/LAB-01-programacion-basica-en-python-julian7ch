"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict
import csv
def pregunta_06():
    with open('./files/input/data.csv',newline='', encoding='utf-8') as archivo:
        lectura = csv.reader(archivo, delimiter='\t')
        listaInteres = []
        nuevaLista = defaultdict(list)
        resultado = []
        for elemento in lectura:
            data = elemento[4]
            tupla = []
            for e in data.split(','):
                clave, valor = e.split(':')
                tupla.append((clave, int(valor)))

            listaInteres.extend(tupla)
        
        for letra, numero in sorted(listaInteres):
            nuevaLista[letra].append(numero)

        for letras, num in nuevaLista.items():
            maxNumero = max(num)
            minNumero = min(num)
            resultado.append((letras, minNumero, maxNumero))
        print(resultado)
        return resultado

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
pregunta_06()