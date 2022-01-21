import turtle
import time
import random


s = turtle.Screen()
s.setup(650, 650)
s.bgcolor('black')

snake = turtle.Turtle()
snake.speed(1)
snake.shape('square')
snake.penup()
snake.goto(0, 0)
snake.direction = 'left'
snake.color('green')

#comida
eat = turtle.Turtle()
eat.shape('circle')
eat.color('orange')
eat.penup()
eat.goto(0,100)
eat.speed(0)

#cuerpo generado por la comida
body = []


def arriba():
    snake.direction = 'up'
def abajo():
    snake.direction = 'down'
def derecha():
    snake.direction = 'right'
def izquierda():
    snake.direction = 'left'


def movimiento():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

#estas son las entradas de teclado (uso teclado 60% por lo que no dispongo de flechas)
s.listen()
s.onkeypress(arriba, 'i')
s.onkeypress(abajo, 'k')
s.onkeypress(derecha, 'l')
s.onkeypress(izquierda, 'j')

#cada vez que algo se mueve, el juego debe actualizarse con un bucle
while True: 
    s.update()


    if snake.distance(eat) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        eat.goto(x, y)

        new_body = turtle.Turtle()
        new_body.shape('square')
        new_body.color('green')
        new_body.penup()
        new_body.goto(0,0)
        new_body.speed(0)
        body.append(new_body)

    full_body = len(body)
    for i in range(-1, 0, -1):
        x = body[i -1].xcor()
        y = body[i -1].ycor()
        body[i].goto(x, y)
    if full_body > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x , y)

    movimiento()



turtle.done()

