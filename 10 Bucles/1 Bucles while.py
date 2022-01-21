#iterador es un contador de repeticiones
#break termina el bucle en algun punto

#vamos a ver WHILE y FOR 

#WHILE necesita iterador (se lo suele llamar como "i" o "j") para no romperse

i = 0 #iterador

while i < 10:
    i += 1
    print("Estoy iterando, voy por el salto: {}".format(i)) #en este caso no se tiene en cuenta el numero 0

while i < 10:
    print("Estoy iterando, voy por el salto: {}".format(i)) #en este caso si se tiene en cuenta el 0 (iterador base)
    i += 1


