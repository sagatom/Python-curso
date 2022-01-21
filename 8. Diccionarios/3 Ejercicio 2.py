diccionario = {1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

jugador = int(input("Ingrese el numero de un jugador: "))

if jugador in diccionario:
    print(diccionario[jugador])
else:
    print("Tu jugador no se encuentra en el diccionario")