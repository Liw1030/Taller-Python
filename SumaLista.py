# 14.Suma de una lista
# Escribe una función que reciba una lista de números y devuelva la suma de todos ellos.

numbers = input('Ingresa los números separados por espacios: ')
lista = list(map(int, numbers.split()))
#* Transformo a una lista de enteros -> list
#* Covierto cada parte en número map(int..)
#* Separo la cadena en partes 4 5 6 a ['4','5','6']

def sumaLista(lista):
    suma = 0 
    for i in lista:
        suma = suma+i
    return suma

resultado = sumaLista(lista)
print('El resultado de la suma es:', resultado)