# função que desenha um poligono regular de n lados
# poligono_regular(numero_lados,comprimeto_lado) . numero_lados  deve ser inteiro e 
# comprimento_lados pode ser inteiro ou float


import turtle

caneta = turtle.Turtle()


def poligono_regular(n_lados, comp_lado,turtle):
    angulo_total = 360/n_lados
    angulo_parcial = 360/n_lados
    while(angulo_total <= 361):
        turtle.forward(comp_lado)
        turtle.setheading(angulo_total)
        angulo_total = angulo_total + angulo_parcial

poligono_regular(7,60,caneta)

 
input()