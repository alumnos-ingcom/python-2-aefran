###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo. (%)
"""

# Funciones// def- return - print - input - if 

def es_par_impar(numero_entero):
    numero_con_dec = numero_entero/2
    numero_dividido = numero_entero//2
    if numero_con_dec != numero_dividido:
        resultado = "es impar"
    else:
        resultado = "es par"

    return resultado
"""
La funcion def es_par_impar llama a la variable numero_entero
La funcion def es_par_impar declara las variables numero_con_dec y numero_dividido
La funcion def es_par_impar compara las variables y determina si es par o impar
La funcion def es_par_impar retorna el valor dentro de la variable resultado
"""
def principal():
    numero_entero=int(input("ingrese un numero entero: "))
    print(es_par_impar(numero_entero))
"""
La funcion def principal pide que se ingrese un numero entero y lo guarda en la variable numero_entero
La funcion def principal mostrara el contenido de la funcion es_par_impar
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""