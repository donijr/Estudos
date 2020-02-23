# para fazer um paralelogramo angulo_1 + angulo_ 2 = 180.

import turtle

caneta = turtle.Turtle()

angulo_total = 0
angulo_1 = 60
angulo_2 = 120
contador = 0
while (contador < 4):
    if (contador % 2 == 0):
        angulo_total= angulo_total + angulo_2
        caneta.forward(100)
        caneta.setheading(angulo_total)
        contador= contador +1
    else:
        angulo_total= angulo_total + angulo_1
        caneta.forward(50)
        caneta.setheading(angulo_total)
        contador= contador +1


input()