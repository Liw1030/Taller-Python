# 18.Frecuencia de letras
# Escribe un programa que cuente la cantidad de veces que aparece cada letra en una palabra dada por el usuario.

palabra = input('Escribe una palabra: ')

cantidadVeces = {}

for letra in palabra:
    if letra in cantidadVeces:
        cantidadVeces[letra] += 1  #* Si la letra ya existe en el diccionario, sumamos 1
    else:
        cantidadVeces[letra] = 1   #* Si no existe, la agregamos con valor 1

print('cantidadVeces de letras:')
for letra, cantidad in cantidadVeces.items():
    print(f'"{letra}" aparece {cantidad} veces')