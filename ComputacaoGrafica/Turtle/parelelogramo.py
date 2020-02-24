# para fazer um paralelogramo angulo_1 + angulo_ 2 = 180.

import turtle

caneta = turtle.Turtle()


def paralelogramo(angulo_1, angulo_2,base,altura,turtle):
    contador = 0
    angulo_total = 0
    while (contador < 4):
        if (contador % 2 == 0):
            angulo_total= angulo_total + angulo_2
            turtle.forward(base)
            turtle.setheading(angulo_total)
            contador = contador +1
        else:
            angulo_total= angulo_total + angulo_1
            turtle.forward(altura)
            turtle.setheading(angulo_total)
            contador= contador +1


paralelogramo(90,90,100,50,caneta)
input()