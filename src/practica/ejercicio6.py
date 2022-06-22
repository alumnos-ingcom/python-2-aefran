###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
El cifrado César o cifrado de rotación usa una encriptación de sustitución simple. Esto significa que cada caracter se sustituye por otro caracter de acuerdo con un sistema especifico.
La codificación debe ser tal que la palabra codificada contenga unicamente caracteres del tipo AZaz y 0 a 9, de manera que al codificar las ultimas letras del abecedario se vuelva a las primeras letras.
Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.
Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
"""

# Funciones// def- return - print - input - if - while -

def codificar_ROT_num(n,cadena):
    i = 0
    lista = list(cadena)
    while i < len(lista):
        if ord(lista[i]) <= 57 and ord(lista[i]) >= 48:
            modulo = ord(lista[i]) + n
            while modulo > 57:
                correccion =  modulo - 57
                modulo =  47 + correccion
            while modulo < 48:
                correccion = 48 - modulo
                modulo= 57 - correccion
            lista[i] = chr(modulo)       
        i = i + 1
    cadena=''.join(lista)        
    return cadena
"""
La funcion def codificar_ROT_num llama a los valores de las variables n y cadena
La funcion def codificar_ROT_num declara las variables i y lista
La funcion def codificar_ROT_num se encarga de identificar los numeron dentro de la cadena y hacer la rotacion segun se especifique en n, guardando los valores en cadena 
La funcion def codificar_ROT_num retorna cadena
"""
def codificar_ROT_minus(n,cadena):
    i = 0
    lista = list(cadena)
    while i < len(lista):
        if ord(lista[i]) <= 122 and ord(lista[i]) >= 97:
            modulo = ord(lista[i]) + n
            while modulo > 122:
                correccion =  modulo - 122
                modulo =  96 + correccion
            while modulo < 97:
                correccion = 97 - modulo
                modulo= 122 - correccion
            lista[i] = chr(modulo)       
        i = i + 1
    cadena=''.join(lista)        
    return cadena
"""
La funcion def codificar_ROT_minus llama a los valores de las variables n y cadena
La funcion def codificar_ROT_minus declara las variables i y lista
La funcion def codificar_ROT_minus se encarga de identificar los caracteres en minuscula y hacer la rotacion segun se especifique en n, guardando los valores en cadena
La funcion def codificar_ROT_minus retorna cadena
"""
def codificar_ROT_mayus(n,cadena):
    i = 0
    lista = list(cadena)
    while i < len(lista):
        if ord(lista[i]) <= 90 and ord(lista[i]) >= 65:
            modulo = ord(lista[i]) + n
            while modulo > 90:
                correccion = modulo -90
                modulo = 64 + correccion
            while modulo < 65:
                correccion = 65 - modulo
                modulo= 90 - correccion

            lista[i] = chr(modulo)       
        i = i + 1
    cadena=''.join(lista)        
    return cadena
"""
La funcion def codificar_ROT_mayus llama a los valores de las variables n y cadena 
La funcion def codificar_ROT_mayus declara las variables i y lista
La funcion def codificar_ROT_mayus se encarga de identificar los caracteres en mayuscula y hacer la rotacion segun se especifique en n, guardando los valores en cadena
La funcion def codificar_ROT_mayus retorna a cadena
"""
def codificar_ROT(n,cadena):
    cadena = codificar_ROT_mayus(n,cadena)
    cadena = codificar_ROT_minus(n,cadena)
    cadena = codificar_ROT_num(n,cadena)
    return cadena
"""
La funcion def codificar_ROT llama a los valores de las variables n y cadena
La funcion def codificar_ROT asigna a cadena los valores de las funciones codficar_ROT_mayus, codficar_ROT_minus y codficar_ROT_num
La funcion def codificar_ROT se encarga de codificar los valores asignados en cadena
La funcion def codificar_ROT retorna cadena
"""
def decodificar_ROT(n,cadena):
    n = (-1)*n
    cadena = codificar_ROT_mayus(n,cadena)
    cadena = codificar_ROT_minus(n,cadena)
    cadena = codificar_ROT_num(n,cadena)
    return cadena
"""
La funcion def decodificar_ROT llama a los valores de las variables n y cadena
La funcion def decodificar_ROT le asigna un nuevo valor a n 
La funcion def decodificar_ROT asigna a cadena los valores de las funciones codficar_ROT_mayus, codficar_ROT_minus y codficar_ROT_num
La funcion def decodificar_ROT se encarga de decodificar los valores asignados en cadena
La funcion def decodificar_ROT retorna cadena
"""
def principal():
    cadena = str(input("ingrese un texto a codificar: "))
    n = int(input("ingrese la rotacion de la codificacion: "))
    cadena= codificar_ROT(n,cadena)
    print(cadena)
    print(decodificar_ROT(n,cadena))
"""
La funcion def principal pide que se ingrese una cadena de texto que sera guardada en la varible cadena
La funcion def principal pide que se ingrese un numero para realizar la rotacion de la cadena y se guarda en la variable n
La funcion def principal declara que la variable cadena tome el valor de la funcion codificar_ROT
La funcion def principal muestra cadena y la funcion decodificar_ROT
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""