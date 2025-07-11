# 4. Tabla de multiplicar
# Escribe un programa que imprima la tabla de multiplicar del 1 al 10 para un número ingresado por el usuario.

num = int(input('Ingresa un número: '))

for i in range(1,11):
    print(i, ' x ', num, ' = ', (i*num)) 