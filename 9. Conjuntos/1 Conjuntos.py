conjuntoejemple = { 1 , 2 , 3 , 4 , 5 } #class set es un conjunto.

#el CONJUNTO se puede utilizar "{}" "set[()]" "set(())" | NO se pueden repetir valores

conjunto = { 1 , 1 , 2 , 3 , 3 , 4 , 5 } 
lista = {1 , 1 , 2 , 3 , 4 , 4 }
print(lista) 
print(conjunto) #los conjuntos no reconocen datos iguales

#metodos

conjunto.add(20) #agregar un dato
conjunto.remove(5) #elimina un dato
conjunto.discard(4) #elimina un valor
conjunto.pop() #no lleva parametro | elimina un valor al azar 
conjunto.update([ 7 , 8 , 9 ]) #agrega elementos iterables (bucle)
conjunto.clear() #vacia el conjunto

