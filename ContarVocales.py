# # 5. Contar vocales
# Pide al usuario una palabra y usa un for para contar cuántas vocales tiene.

frase = input('Por favor ingresa una palabra: ')
contador = 0
for letra in frase:
    if letra in 'a,e,i,o,u':
        contador = contador+1

print('La palabra ',frase, ' tiene: ',contador, 'vocales')