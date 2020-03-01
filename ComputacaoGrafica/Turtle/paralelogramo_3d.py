# para fazer um paralelogramo angulo_1 + angulo_ 2 = 180.
# !!! Restrições do Algoritmo: Foi testado em algumas combinações de angulo_1 e angulo_2 e não obtive o
# resultados esperado, mas em compensação na maioria o efeito 3D é bem sucedido

import turtle

caneta = turtle.Turtle()


def paralelogramo(angulo_1, angulo_2,base,altura,profundidade,turtle):
    posicao_desenho_inicial = turtle.pos()
    contador = 0
    angulo_total = 0
    while (contador < 4):
        if (contador % 2 == 0):
            posicao_poligono = turtle.pos()
            posicao_linha = posicao_poligono + (profundidade,profundidade)
            turtle.setpos(posicao_linha)
            turtle.penup()
            turtle.setpos(posicao_poligono)
            turtle.pendown()
            angulo_total= angulo_total + angulo_2
            turtle.forward(base)
            turtle.setheading(angulo_total)
            contador = contador +1
        else:
            posicao_poligono = turtle.pos()
            posicao_linha = posicao_poligono + (profundidade,profundidade)
            turtle.setpos(posicao_linha)
            turtle.penup()
            turtle.setpos(posicao_poligono)
            turtle.pendown()
            angulo_total= angulo_total + angulo_1
            turtle.forward(altura)
            turtle.setheading(angulo_total)
            contador= contador +1

    nova_posicao_desenho = posicao_desenho_inicial + (profundidade,profundidade)
    turtle.setpos(nova_posicao_desenho)

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


paralelogramo(70,110,100,50,50,caneta)
input()