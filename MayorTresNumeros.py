# 3. Mayor de tres números
# Pide tres números al usuario e imprime cuál es el mayor.

print('Ingresa 3 números, vamos a ver cual es el mayor')

num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
num3 = int(input('Ingresa el tercer número: '))

if num1 > num2 and num1 > num3:
    print('El número mayor es: ', num1)
elif num2 > num1 and num2 > num3:
    print('El número mayor es', num2)
elif num3 > num1 and num3 > num2:
    print('El número mayor es', num3)
else:
    print('Todos los números son iguales')