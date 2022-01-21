# Ejercicio 1 

palabra1 = input("Ingrese la primer palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman porque tienen menos de 3 caracteres")
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print("Las palabras riman")
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras NO")





# Ejercicio 2 

voto = input("Elija un candidato por el cual votar (A partido ROJO, B partido VERDE o C partido AZUL): ")

if voto.lower() == "a":
    print("Usted ha votado por el partido ROJO")
elif voto.lower() == "b":
    print("Usted ha votado por el partido VERDE")
elif voto.lower() == "c":
    print("Usted ha votado por el partido AZUL")
else:
    print("Opción errónea")