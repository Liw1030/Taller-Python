# 13.Contar palabras
# Crea una función que reciba una cadena y devuelva cuántas palabras contiene.

prase = input('Ingresa una frase: ')

def contarPalabras(prase):
    palabras = prase.split() #* Aqui divido la frase en palabras "Hola mundo bonito" → ["Hola", "mundo", "bonito"] (las separa por espacios)
    cantidad = len(palabras) #* Len() me dice cuantos elemetos hay en la variable palabras = ["Hola", "mundo", "bonito"]
    return cantidad

cantidadPalabras = contarPalabras(prase)
print('La frase tiene:', cantidadPalabras, 'palabras.')