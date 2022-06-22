###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas. Siendo 0 sin superposición y uno para cada elemento superpuesto.

['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
y

['H', 'o', 'l', 'a']
Tienen una superposición de cuatro elementos.
"""

# Funciones// def- return - print - input - if - while -

def calcular_superposicion(lista_uno, lista_dos):
    i = 0
    coincidencia=0
    coincidencias=0
    while i < len(lista_uno):
        if coincidencia < len(lista_dos):
            if lista_uno[i] == lista_dos[coincidencia]:
                coincidencia =  coincidencia + 1
                coincidencias = coincidencias + 1
            else: 
                coincidencia = 0
        i = i + 1
    return coincidencias
"""
La funcion def calcular_superposicion pide los valores de las varibles lista_uno y lista_dos
La funcion def calcular_superposicion declara las variables i, coincidencia y coincidencias
La funcion def calcular_superposicion comprueba los valores asociados a las variables lista_uno con los de lista_dos y en cason de haber una coincidencia en algun valor lo suma a la variable
La funcion def calcular_superposicion retorna el valor de coincidencias
"""
def principal():
    i=0
    lista_uno = []
    texto = str(input("ingrese la cadena de texto: "))
    while i < len(texto):
        lista_uno = lista_uno + [texto[i]]
        i = i + 1
    i=0
    lista_dos = []
    texto = str(input("ingrese la cadena de texto de superposicion: "))
    while i < len(texto):
        lista_dos = lista_dos + [texto[i]]
        i = i + 1
    print(calcular_superposicion(lista_uno, lista_dos))

"""
La funcion def principal declara las varibles i y lista_uno
La funcion def principal pide que se ingrese una cadena de texto y la guarda en la variable texto
La funcion def principal en caso de que lista_dos sea igual a si misma + el valor de texto le añade a la variable i un valor (i+1)
La funcion def principal muestra el valor de la funcion calcular_superposicion
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""