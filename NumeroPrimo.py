# 10.Número primo
# Pide un número al usuario y determina si es primo (divisible solo por 1 y por sí mismo).

num = int(input('Ingresa un número para determinar si es primo: '))

if num < 2:
    print("El número no es primo.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("El número no es primo.")
            break
    else:
        print("El número es primo.")