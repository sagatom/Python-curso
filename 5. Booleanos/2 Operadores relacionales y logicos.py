#Operadores Relacionales son y sirven para hacer comparaciones
'''
== igual que... 5 == --> False

!= diferente de ... 5 != 3 --> True

< menor que... 6 < 20 --> True 

> mayor que... 100 > 1 --> True

<= menor o igual que... 90 <= 90 --> True

>= mayor o igual que... 100 >= 101 --> False'''

#Operadores Logicos son comparaciones 

'''
and | y | 10 > 1 and 70 <= 70 --> True | ambas comparaciones deben ser verdaderas para ser considerado verdadero

or | o | 50 >= 80 or 6 == 6 --> True | si ambas o una de las comparaciones es verdadera se considera verdadero

not | no a... | 3.14 > 3 --> True --> False'''

num1 = 1000
num2 = 500
cadena = "Comparaciones de strings"
cadena2 = "Comparacion de string"

print(num1 > num2)
print(num2 > num1)
print(num1 == num2)
print(num1 != num2) #como las variables son diferentes devuelve True
print(cadena > cadena2) #Cadena tiene mas letras que cadena2 por lo que devuelve true


