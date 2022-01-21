diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": 
"Tegucifalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", 
"Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('Ingrese un pais para conocer su capital: ')

if pais.capitalize() in diccionario:
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario")