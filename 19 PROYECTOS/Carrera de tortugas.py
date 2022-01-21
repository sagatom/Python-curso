import turtle
import random

s = turtle.Screen()
s.title("Carrera de tortugas")
s.bgcolor("black")

player1 = turtle.Turtle()
player2 = turtle.Turtle()

player1.hideturtle()
player1.shape("turtle")
player1.color("green", "green")
player1.shapesize(2,2,2)
player1.pensize(3)

player2.hideturtle()
player2.shape("turtle")
player2.color("blue", "blue")
player2.shapesize(2,2,2)
player2.pensize(3)

player1.penup()
player1.goto(300, 150)
player1.pendown()
player1.circle(40)

player2.penup()
player2.goto(300, -150)
player2.pendown()
player2.circle(40)

player1.penup()
player1.goto(-300, 175)
player1.pendown()
player1.showturtle()

player2.penup()
player2.goto(-300, -125)
player2.pendown()
player2.showturtle()

dado = [ 1 , 2 , 3 , 4 , 5 , 6 ]

for i in range(20):
    if player1.pos() >= (300, 150):
        print("La tortuga VERDE ha ganado")
        break
    elif player2.pos() >= (300, -150):
        print("La turtuga AZUL ha ganado")
        break
    else:
        turno1 = input("Presiona la tecla ENTER para avanzar")
        turno1 = random.choice(dado)
        print("tu numero es: ",turno1, "\nAvanzas: ", turno1*20)
        player1.forward(20*turno1)

        turno2 = input("Presiona la tecla ENTER para avanzar")
        turno2 = random.choice(dado)
        print("tu numero es: ",turno2, "\nAvanzas: ", turno2*20)
        player2.forward(20*turno2)





turtle.done()