# 19.Números perfectos
# Escribe un programa que encuentre los números perfectos entre 1 y 1000. Un número perfecto es igual a la suma de sus divisores (excluyendo el propio número).

print('Vamos a encontrar los números perfectos entre 1 y 1000')

for numero in range(1, 1001):  
    suma = 0  
    for divisor in range(1, numero):
        if numero % divisor == 0: 
            suma += divisor       
    if suma == numero:
        print(f'{numero} es un número perfecto')