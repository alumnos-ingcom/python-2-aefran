###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine si una cadena con corchetes está balanceada.
Es decir, si cada corchete que abre, tiene su par que cierra. El resultado debe ser un valor lógico indicando si esta o no balanceado.
"""

# Funciones// def- return - print - input - if - while -

def balanceador_de_corchetes(cadena):
    i=0
    balanceado = True
    contador = 0
    while i < len(cadena):
        if cadena[i] == '[':
            contador = contador + 1
        if cadena[i] == ']':
            contador = contador - 1
        if contador == -1:
            balanceado = False
        i = i + 1
    if contador > 0:
        balanceado = False
    return balanceado
"""
La funcion def balanceador_de_corchetes llama a el valor guardado en cadena
La funcion def balanceador_de_corchetes declara las variables i, balanceado y contador
La funcion def balanceador_de_corchetes determina que en caso de que haya un corchete de mas o uno menos, la cadena estara no balanceada. Y en caso de que haya la misma cantidad de corchetes "[" que de "]" te mostrara que esta balanceado
La funcion def balanceador_de_corchetes retorna el valor de balanceado
"""
def principal():
    cadena=str(input("ingrese una cadena de corchetes: "))

    print(balanceador_de_corchetes(cadena))
"""
La funcion def principal pide que se ingrese la cedena de corchetes y la guarda en la variable cadena
La funcion def principal muestra el valor de la funcion balanceador_de_corchetes
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""