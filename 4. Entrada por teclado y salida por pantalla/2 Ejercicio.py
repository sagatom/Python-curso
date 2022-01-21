from math import sqrt #importa raiz cuadrada


#Ejercicio 1 el ejercicio esta mal pero es a modo de ejemplo 

a = int(input('ingrese el valor de "a": '))
b = int(input('ingrese el valor de "b": '))
c = int(input('ingrese el valor de "c": '))

if ((b ** 2)-( 4 * a * c )) < 0:
    print('No se puede realizar porque no se puede sacar raiz a un numero negativo')
else:
    solucion = (-b + sqrt ((b ** 2) - (4 * a * c)) / (2 * a))
    print('La solucion es: ' + solucion)


#Ejercicio 2

p1 = float(input('Ingrese nota del primer trabajo practico: '))
p2 = float(input('Ingrese nota del segundo trabajo practico: '))
p3 = float(input('Ingrese nota del tercer trabajo practico: '))
pp = ( p1 + p2 + p3 ) / 3
ep = float(input('Ingrese nota del examen parcial: '))
ef = float(input('Ingrese nota del examen final: '))
prom = ( pp + ep + ef ) / 3

print('Su promedio es: ' + prom)