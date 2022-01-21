def suma():
    global num1 #definiendo asi la funcion se puede usar dentro y fuera de la funcion 
    global num2
    num1 = 110
    num2 = 40
    suma = num1 + num2
    return suma

print(suma(20 , 30))
print(suma(100 , 50))

resta = num1 - num2
print(resta)