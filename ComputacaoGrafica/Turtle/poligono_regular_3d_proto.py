import turtle

caneta = turtle.Turtle()


def poligono_regular(n_lados, comp_lado,turtle):
    angulo_total = 360/n_lados
    angulo_parcial = 360/n_lados
    while(angulo_total <= 361):
        turtle.forward(comp_lado)
        turtle.setheading(angulo_total)
        angulo_total = angulo_total + angulo_parcial

def poligono_regular2(n_lados, comp_lado,turtle):
    """ x_atual = 0
    y_atual = 0
    y_temp = 0
    x_temp = 0 """
    angulo_total = 360/n_lados
    angulo_parcial = 360/n_lados
    while(angulo_total <= 361):
        x_atual = turtle.xcor()
        y_atual = turtle.ycor()
        x_temp = x_atual + 50
        y_temp = y_atual + 50
        turtle.setpos(x_temp,y_temp)
        turtle.penup()
        turtle.setpos(x_atual,y_atual)
        turtle.pendown()
        turtle.forward(comp_lado)
        turtle.setheading(angulo_total)
        angulo_total = angulo_total + angulo_parcial

caneta.speed(1)
caneta.fillcolor('red')
caneta.begin_fill()
poligono_regular2(4,100,caneta)
caneta.speed(1)
caneta.setpos(50,50)
caneta.speed(1)
poligono_regular(4,100,caneta)
caneta.end_fill()




""" #mult1 = 
mult2= 10
for i in range(10):
    poligono_regular(7,60,caneta)
    caneta.setpos(0,mult2)
    #mult1 =+ mult1
    mult2 =+ mult2

#caneta.setpos(4*(caneta.pos()))
caneta.setpos(60,120)
poligono_regular(7,60,caneta) """
input()