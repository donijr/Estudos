#n_pontas = número de pontas da estrela. n_lados deve ser do tipo inteiro
#comp_lado = comprimento do total de uma ponta a outra da estrela. comprimento pode ser tipo inteiro ou float
#turtle = objeto do tipo turtle que vai desenhar o polígono

# !!! Restrições do algoritmo: Ainda não aperfeicoei, então para conseguir resultados satisfatórios n_lados >= 5 e sempre ímpar. 
# a partir de certo número de n_lados o desenho não fica muito mais definido.

import turtle

def estrela_tipo_mandala(n_pontas,comprimento,turtle):
    for i in range(n_pontas):
        angulo = 360 / n_pontas
        turtle.right(angulo*2)
        turtle.forward(comp_lado)

caneta = turtle.Turtle()

estrela_tipo_mandala(9,70,caneta)

input()
