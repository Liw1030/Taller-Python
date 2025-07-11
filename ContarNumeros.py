# 6. Números del 1 al N
# Pide al usuario un número N e imprime todos los números del 1 al N usando un while.

num = int(input('Ingresa un número: '))
contador = 1

while contador < num+1:
    print(contador)
    contador = contador+1