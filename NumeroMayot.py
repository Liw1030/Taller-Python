# 12.Número mayor
# Escribe una función que reciba tres números y devuelva el mayor de ellos.

print('Hola, dame tres número y te diré el mayor: ')

num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Tercer número: '))

def numeroMayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return 'Todos los números son iguales'

resultado = numeroMayor(num1, num2, num3)
print('El número mayor es:', resultado)
