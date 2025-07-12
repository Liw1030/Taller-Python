# 15.Es palíndromo
# Crea una función que determine si una palabra es un palíndromo (se lee igual al derecho y al revés). Da un mensaje, si no lo es.

print('Escribe una palabra para descubrir si es un palíndromo')

palabra = input('Ingresa una palabra: ')

def esPolindromo(palabra):
    voltear = palabra[::-1] #* Esto -> [::-1] es una técnica para invertir la palabra ejemplo: Oso -> osO
    if palabra == voltear:
        return 'La palabra es un políndromo'
    else:
        return 'La palabra NO es un políndromo'
    
resultado = esPolindromo(palabra)
print(resultado)