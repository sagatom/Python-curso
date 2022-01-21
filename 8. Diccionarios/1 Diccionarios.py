diccionarioejemplo = {'Usuario' : "tsagasta" , 'Contrasena' : 12345}   #necesito 'clave' y "valor"

print(diccionarioejemplo)

#Elementos diccionario

diccionario = {'Nombre' : "Sagasta" , 'Apellido' : "Sagasta" , "Estatura" : 1.87}

print(diccionario.keys()) #muestra las claves (llaves)
print(diccionario.values()) #muestra los valores

print(diccionario["Estatura"])  #mandar a llamar un valor correspondiente a una clave

diccionario["Peso"] = "95 kg" #agregar o modificar un dato
print(diccionario)

diccionario1 = { 1 : 2 , 2 : 3 , 3 : 4 }
diccionario2 = {4 : 5 , 5 : 6 , 6 : 7}

print(diccionario1)

diccionario1.pop(3)  #metodo que elimina la ultima clave (llave)
diccionario1.get(2) #metodo que usas para traer el valor de alguna clave (llave)
diccionario1.setdefault(4 , 5) #agrega clave y valor al final
diccionario1.update(1 , 50) #modifica un valor de una clave en particular 
diccionario1.update(diccionario2) 
print(diccionario1)
diccionario1.copy(diccionario2) #genera una copia de otro diccionario
diccionario1.clear() #metodo que borra todo el diccionario