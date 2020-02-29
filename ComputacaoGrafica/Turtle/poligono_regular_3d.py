#n_lados = número de lados do polígono. n_lados deve ser do tipo inteiro
#comp_lado = comprimento do lado do polígono. comp_lado pode ser tipo inteiro ou float
#profundidade = profundidade do polígono. profundidade pode ser tipo inteiro ou float
#turtle = objeto do tipo turtle que vai desenhar o polígono

import turtle

caneta = turtle.Turtle()

def poligono_regular_3d(n_lados, comp_lado,profundidade,turtle):
    posicao_desenho_inicial = turtle.pos()
    acumulador_angulo = 360/n_lados
    angulo_minimo = 360/n_lados

    while(acumulador_angulo <= 361):
        posicao_poligono = turtle.pos()
        posicao_linha = posicao_poligono + (profundidade,profundidade)
        turtle.setpos(posicao_linha)
        turtle.penup()
        turtle.setpos(posicao_poligono)
        turtle.pendown()
        turtle.forward(comp_lado)
        turtle.setheading(acumulador_angulo)
        #acumulador_angulo = acumulador_angulo + angulo_minimo
        acumulador_angulo += angulo_minimo


    nova_posicao_desenho = posicao_desenho_inicial + (profundidade,profundidade)
    turtle.setpos(nova_posicao_desenho)

    acumulador_angulo = 360/n_lados
    while(acumulador_angulo <= 361):
        turtle.forward(comp_lado)
        turtle.setheading(acumulador_angulo)
        #acumulador_angulo = acumulador_angulo + angulo_minimo
        acumulador_angulo += angulo_minimo

caneta.setpos(-50,-50)

poligono_regular_3d(5,100.587,50.4587,caneta)

input()
