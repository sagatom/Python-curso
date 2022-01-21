def numeros():
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0
print(numeros())