# função que desenha um poligono regular de n lados
# poligono_regular(numero_lados,comprimeto_lado) . numero_lados  deve ser inteiro e 
# comprimento_lados pode ser inteiro ou float


import turtle

caneta = turtle.Turtle()


def poligono_regular(n_lados, comp_lado,turtle):
    acumulador_angulo = 360/n_lados
    angulo_minimo = 360/n_lados
    while(acumulador_angulo <= 361):
        turtle.forward(comp_lado)
        turtle.setheading(acumulador_angulo)
        #acumulador_angulo = acumulador_angulo + angulo_minimo
        acumulador_angulo += angulo_minimo

poligono_regular(7,60,caneta)

 
input()