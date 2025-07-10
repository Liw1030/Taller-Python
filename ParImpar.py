# 2. Par o impar
# Pide un número al usuario y determina si es par o impar usando if.

print('Vamos a descubrir si el número es par o impar')

num = float(input('Ingresa el número que quieres validar: '))

if num % 2 == 0:
    print('El número que ingresaste SÍ es par')
else:
    print('El número ingresado NO es par :(')

