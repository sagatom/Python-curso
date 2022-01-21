import turtle

s = turtle.Screen()
t = turtle.Turtle()


t.speed(2) #esto le da velocidad del 1 al 10


t.goto(100,100)
t.goto(-100,100)
t.hideturtle()
t.circle(10)
t.circle(50)
t.dot(30)  #es un circulo relleno de diametro 30
t.showturtle()
t.setx(100) #mantiene el eje X y se desplaza 100 unidades en el Y
t.sety(50)  #mantiene el eje Y y se desplaza 100 unidades en el X




turtle.done()
