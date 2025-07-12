# 17.Invertir una cadena
# Crea una función que reciba una cadena y devuelva la cadena invertida (por ejemplo,"hola" -> "aloh").

print('Escribe una palabra y la voltearemos')

palabra = input('Ingresa una palabra: ')

def voltearPalabra(palabra):
    voltear = palabra[::-1] #* Esto -> [::-1] es una técnica para invertir la palabra ejemplo: Oso -> osO
    return voltear
    
resultado = voltearPalabra(palabra)
print(resultado)