###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores.
En la misma, los dos primeros términos son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1) 
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""

# Funciones// def- return - print - input - if - while -

def fibonacci(n):
    n = n-2
    valor_anterior=1
    valor=1
    while n>0:
        valor_nuevo = valor + valor_anterior
        valor_anterior = valor
        valor = valor_nuevo
        n = n - 1
    return valor
"""
La funcion def fibonacci llama a el valor guardado en la variable n
La funcion def fibonacci declara las variables valor_anterior y valor
La funcion def fibonacci transforma el valor de n
La funcion def fibonacci calcula el n-esimo valor de la serie de fibonacci, guardandolo en la variable valor
La funcion def fibonacci retorna valor
"""
def principal():
    n=int(input("ingrese el valor n-esimo valor deseado: "))
    print(fibonacci(n)) 

"""
La funcion def principal pide que se ingrese un valor, que sera guardado en la variable n
La funcion def principal muestra el n-esimo valor guardado en la funcion fibonacci
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""