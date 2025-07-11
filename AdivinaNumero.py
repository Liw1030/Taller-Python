# 9. Adivina el número
# Genera un número aleatorio entre 1 y 10 (usa random.randint) y permite al usuario
# adivinarlo.
# Da pistas como "muy bajo" o "muy alto".

import random
numeroSecreto = random.randint(1, 10)

intento = int(input("Adivina el número (1-10): "))

while intento != numeroSecreto:
    if intento < numeroSecreto:
        print("Muy bajo.")
    else:
        print("Muy alto.")
    intento = int(input("Intenta de nuevo: "))

print("¡Correcto! Adivinaste el número.")
