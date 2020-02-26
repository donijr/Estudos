#Documentação Turtle: https://docs.python.org/3.3/library/turtle.html#

import turtle

tartaruga = turtle.Turtle()

#tartaruga.position() # indica as cordenadas do vetor em que tartaruga está. Inicia em (0.00,0.00)
#tartaruga.pos()
print(tartaruga.pos())
# turtle.forward(distancia) - move a turtle para frente por uma distancia especifica
# turlte.fd(distancia)
tartaruga.forward(25) # desenha linha de 25 pixel e termina em (25.00,0.00)
tartaruga.forward(-75) # termina em (-50.00,0.00) . antes estava em (25.00,0.00).

# turlte.backarward(distancia) - move a turtle para trás por uma distância especifica. Move na direção oposta em que a turtle está indo.
# turlte.bk(distancia)
# turtle.back(distancia)
tartaruga.backward(25)

# turtle.right(angulo) - vira a turtle para a direita x graus. angulo é um numero inteiro ou float
# turtle.rt(angulo)

tartaruga.right(90)

# turtle.left(angulo) - vira a turtle para a esquerda x graus. angulo é um numero inteiro ou float
# turtle.lt(angulo)
tartaruga.left(90)

#turtle.setpos(x, y=None) - move a turtle para uma posicao (x,y) em um vetor 2D
#turtle.goto(x, y=None)
#turtle.setposition(x, y=None)
#OBS: Se pen is down ele desenha uma linha. A turtle não muda de direção. Por exemplo se o angulo da
# turtle é 90, então vai fazer uma linha da posicao de origem a até setpos(x,y) em um angulo de 90º
tartaruga.setpos(150,20)

#turtle.setx(x) - altera somente a coordenada x da posicao da tartaruga, a y fica inalterada. 
# x é um número inteiro ou float. Se caneta abaixada ela continua desenhando
tartaruga.setx(50)

#turtle.sety(y) - altera somente a coordenada y da posicao da tartaruga, a x fica inalterada. 
# y é um número inteiro ou float. Se caneta abaixada ela continua desenhando
tartaruga.sety(60)

# turtle.setheading(angulo) - Define a orientação do ângulo em que a a turtle deve estar. Basicamente 
#ele gira a turtle em determinado ângulo sem movê-la do lugar. angulo é um número inteiro ou float
# turtle.seth(to_angle)
tartaruga.setheading(180)

#turtle.home() - Move a turtle para a origem coordenada (0,0) e define a orientação da turtle como a orientação 
#inicial ( vai depender do modo em que ela está: “standard”, “logo” ou “world”. Ver mode()). Se caneta abaixada
#continua desenhando
tartaruga.home()




input()