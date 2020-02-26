import turtle

caneta = turtle.Turtle()
# >>>> ---------------------------- <<<<
# >>>> Desenhar poligonos Regulares <<<<
# >>>> ---------------------------- <<<<

#caneta.circle(tamanho_raio,360,numero_lados)
#Se quiser que o poligono comece em determinada orientação usar .setheding(angulo) antes de desenhar
#Exemplo com quadrado
caneta.setheading(45)
caneta.circle(100,360,4)
print(caneta.heading())
input()