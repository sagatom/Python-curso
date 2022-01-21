class calculadora():
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
    
    def suma(self):
        self.suma = self.valor1 + self.valor2
        print("La suma es de: ",self.suma)
    
    def resta(self):
        self.resta = self.valor1 - self.valor2
        print("La resta es de: ",self.resta)
    
    def multiplicacion(self):
        self.multiplicacion = self.valor1 * self.valor2
        print("La multiplicacion es de: ",self.multiplicacion)
    
    def division(self):
        self.division = self.valor1 / self.valor2
        print("La division es de: ",self.division)

calcular = calculadora()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()