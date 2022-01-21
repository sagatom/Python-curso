'''Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno'''

class fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class auto(fabrica):
    def datos(self):
        print("La cantidad de llantas del auto es de: ",self.llantas)
        print("El color del auto es de: ",self.color)
        print("El precio del auto es de: $",self.precio)

class moto(fabrica):
    def datos(self):
        print("La cantidad de llantas de la moto es de: ",self.llantas)
        print("El color de la moto es de: ",self.color)
        print("El precio de la moto de: $",self.precio)

moto = moto(2, "Negro", 4000)
moto.datos()

auto = auto(4, "Blanco", 15000)
auto.datos()

