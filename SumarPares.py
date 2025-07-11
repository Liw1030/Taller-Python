# # 8. Sumar números pares
# Usa un for para sumar todos los números pares entre 1 y 100.

suma = 0

# for i in range(empieza en 0, va hasta el 100, sube de 2 en dos)
for i in range(0, 101, 2):  
    suma += i  

print("La suma de los números pares del 1 al 100 es:", suma)
