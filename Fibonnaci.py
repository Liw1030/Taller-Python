# 16.Fibonacci
# Escribe una función que genere los primeros N números de la secuencia de Fibonacci.


def secuenciaFibonacci(n):
    a = 0
    b = 1
    lista = []
    for i in range(n):
        lista.append(a)
        siguiente = a + b
        a = b
        b = siguiente
    return lista

resultado = secuenciaFibonacci(10)
print('La secuencia de Fibonacci es:', resultado)