# 11.Área de un triángulo
# Crea una función que calcule el área de un triángulo dados su base y altura.

print('Vamos a calcular el área de un triangulo')

base = int(input('Ingresa la base del triangulo: '));
altura = int(input('Ingresa la altura del triangulo: '));

def areaTriagulo(base, altura):
    area = (base * altura)/2
    return area

resultadoArea = areaTriagulo(base,altura)

print('El área del triangulo es: ', resultadoArea)