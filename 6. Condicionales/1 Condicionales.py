'''
if si se cumple esta condicion lo ejecuta
else si no se cumple if se realiza else 
elif sirve para multiples escenarios 

'''

# ejemplo como saber que si una parsona es mayor o igual de edad

edad = 17

if edad >= 18:
    print("Tu eres mayor de edad. Puedes tomar alcohol")
else: 
    print("Tu no puedes tomar alcohol, vete a dormir crio")

letra = "I"

if letra.lower() == "a":          #se ingresa lower para que te tome la letra mayuscula o minuscula
    print("Esta vocal es la A") 
elif letra.lower() == "e":
    print("Esta vocal es la E")
elif letra.lower() == "i":
    print("Esta vocal es la I")
elif letra.lower() == "o":
    print("Esta vocal es la O")
else:                             #para el cierre de las condiciones se utiliza else, ya que no quedaria mas opciones
    print("Esta vocal es la U")