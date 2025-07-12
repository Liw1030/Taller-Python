# 20.Menú interactivo
# Diseña un programa que muestre un menú al usuario con opciones como:
# 1. Calcular el cuadrado de un número.
# 2. Mostrar números pares entre dos valores.
# 3. Salir del programa.
# Usa un bucle while para mantener el menú activo hasta que el usuario elija
# salir.


opcion = 0  

while opcion != 3:
    print('Escoge una opción: ')
    print('1. Calcular el cuadrado de un número')
    print('2. Mostrar números pares entre dos valores')
    print('3. Salir del programa')

    opcion = int(input('Elige una opción: '))

    if opcion == 1:
        numero = int(input('Ingresa un número: '))
        cuadrado = numero ** 2
        print('El cuadrado de' ,numero, 'es:', cuadrado)

    elif opcion == 2:
        num1 = int(input('Ingresa el primer número: '))
        num2 = int(input('Ingresa el segundo número: '))
        print('Los números pares entre:', num1, 'y', num2, 'son:')
        for n in range(num1, num2 + 1):
            if n % 2 == 0:
                print(n)

    elif opcion == 3:
        print('Graciassss')

    else:
        print('Opción no válida. Por favor, elige 1, 2 o 3.')