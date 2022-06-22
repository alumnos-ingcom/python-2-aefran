###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""

# Funciones// def- return - print - input - if - while -

def max(lista):
    i = 0
    salida = lista[0]
    while i < len(lista):
        if salida < lista[i]:
            salida = lista[i]
        i = i + 1
    return salida
"""
La funcion def max llama a la variable lista
La funcion def max declara las variables i y salida 
La funcion def max dentro de los valores de lista determina cual posee el valor mas alto
La funcion def max retorna salida
"""
def prom(lista):
    i = 0
    salida = 0
    while i < len(lista):
        salida = salida + lista[i]
        i = i + 1
    salida = salida//len(lista)
    return salida 
"""
La funcion def prom llama a la variable lista
La funcion def prom declara las variables i y salida
La funcion def prom dentro de los valores de lista determina el promedio de la suma de los valores
La funcion def prom retorna salida
"""
def min(lista):
    i = 0
    salida = lista[0]
    while i < len(lista):
        if salida > lista[i]:
            salida = lista[i]
        i = i + 1
    return salida
"""
La funcion def min llama a la variable lista
La funcion def min declara las varibles i y salida
La funcion def min determina cual es el menor de los valores de lista
La funcion def min retorna salida
"""
def max_min_prom(lista):
    salida = (max(lista), min(lista), prom(lista))
    return salida
"""
La funcion def max_min_prom llama a la variable lista
La funcion def max_min_prom guarda en salida los valores de las funciones max, min y prom
La funcion def max_min_prom retorna salida
"""
def principal():
    opciones = 0
    lista=[]
    while opciones < 2:
        lista = lista + [int(input("ingrese un numero a la lista: "))]
        opciones = int(input("desea ingresar otro numero\n1. si\n2. no\n")) 
    print(max_min_prom(lista))

"""
La funcion def principal declara las varibles opciones y lista
La funcion def principal pide que mientras se cumpla que opciones se mayor a 2 se pida si el usuario quiere ingresar otro valor y los va guardando en la variable lista
La funcion def principal mostrara los valores de la funcion max_min_prom
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""