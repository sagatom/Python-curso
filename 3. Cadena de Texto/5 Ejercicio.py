cadena = "Te quiero solo como amigo"

print(cadena[0:2])
print(cadena[-3:])
print(cadena[ : : 2 ]) # hace una copia e imprime cada 2 caracteres
print(cadena[: :-1]) #hace una copia e imprime la cadena invertida
print(cadena + cadena[: : -1])

palabra = "Separado"

print(palabra)

reemplazar = palabra.replace("" , ",")
print(reemplazar)