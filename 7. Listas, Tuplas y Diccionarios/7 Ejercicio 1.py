lista = [ 20 , 50 , "Curso" , 'Phyton' , 3.14 ]
print("Los valores de la lista son los siguientes: ", lista)

valor1 = input("Ingrese un valor a la lista: ")
lista[0] = valor1

valor2 = input("Ingrese un nuevo valor a la lista: ")
lista[1] = valor2

print("Los nuevos valores de la lista son los siguientes: {}".format(lista))