#Ejercicio 1 Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input("Ingresa una letra: ")

if letra.lower() == "a":
    print("Es vocal")
elif letra.lower() == "e":
    print("Es vocal")
elif letra.lower() == "i":
    print("Es vocal")
elif letra.lower() == "o":
    print("Es vocal")
elif letra.lower() == "u":
    print("Es vocal")
else:
    print("NO es una vocal")


#Ejercio 2 Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numero = int(input("Ingrese un numero: "))

if numero >= 0:
    print("el valor absoluto de {} es: {}".format(numero, numero))
else:
    print("el valor absoluto de {} es: {}".format(numero, numero * -1)) # "abs(numero)" tmb da el valor absoluto

