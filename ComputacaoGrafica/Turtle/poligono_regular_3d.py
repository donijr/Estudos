import turtle

caneta = turtle.Turtle()


def poligono_regular(n_lados, comp_lado,turtle):
    acumulador_angulo = 360/n_lados
    angulo_minimo = 360/n_lados
    while(acumulador_angulo <= 361):
        turtle.forward(comp_lado)
        turtle.setheading(acumulador_angulo)
        acumulador_angulo = acumulador_angulo + angulo_minimo

def poligono_regular_3d(n_lados, comp_lado,deslocamento,turtle):
    acumulador_angulo = 360/n_lados
    angulo_minimo = 360/n_lados
    while(acumulador_angulo <= 361):
        x_atual = turtle.xcor()
        y_atual = turtle.ycor()
        x_temp = x_atual + deslocamento
        y_temp = y_atual + deslocamento
        turtle.setpos(x_temp,y_temp)
        turtle.penup()
        turtle.setpos(x_atual,y_atual)
        turtle.pendown()
        turtle.forward(comp_lado)
        turtle.setheading(acumulador_angulo)
        acumulador_angulo = acumulador_angulo + angulo_minimo
caneta.setpos(100,100)
print(caneta.pos())
posicao_inicial = caneta.pos()
nova_pos = posicao_inicial + (50.00,50.00)
print(nova_pos)

""" deslocamento = 70
caneta.speed(1)
poligono_regular_3d(6,100,70,caneta)
caneta.speed(1)
caneta.setpos(deslocamento,deslocamento)
caneta.speed(1)
poligono_regular(6,100,caneta)
caneta.end_fill()
 """




input()