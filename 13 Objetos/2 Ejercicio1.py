class alumno():
    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Tu nombre: ", self.nombre)
        print("Tu nota: ", self.nota)

    def resultado(self):
        if self.nota < 5:
            print("Has reprobado")
        else:
            print("Has aprobado")

alumno1 = alumno()
alumno1.datos("Carlos", 3)

alumno2 = alumno()
alumno2.datos("Michelle", 9)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()