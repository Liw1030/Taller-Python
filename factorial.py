# 7. Factorial
# Escribe un programa que calcule el factorial de un número usando un for.

number = int(input('Ingresa un número: '))
factorial = 1 

for i in range(1, number + 1):  
    factorial *= i  # factorial = factorial * i

print('El factorial de', number, 'es:', factorial)
