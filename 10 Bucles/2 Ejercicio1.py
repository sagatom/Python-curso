numero = int(input("Ingresa un numero pasa saber su tabla: "))
i = 0 #iterador
multi = 0

while i <= 10:
    multi = numero * i
    print("{} x {} = {}".format(numero , i , multi)) #en este caso si se tiene en cuenta el 0 (iterador base)
    i += 1 