# função que desenha um poligono regular de n lados
# poligono_regular(numero_lados,comprimeto_lado) . numero_lados e comprimento_lados devem ser inteiros
# Dependendo do número de lados a função arredonda o número do ângulo para um inteiro.

import turtle

caneta = turtle.Turtle()


def poligono_regular(n_lados, comp_lado):
    n_lados = int(360/n_lados)
    for i in range(n_lados,361,n_lados):
        caneta.forward(comp_lado)
        caneta.setheading(i) 

poligono_regular(7,50)

 
input()