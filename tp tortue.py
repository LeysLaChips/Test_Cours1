import turtle
import random
maTortue = turtle.Turtle()
maTortue.speed= 0
turtle.delay(0)


#square
"""
maTortue.speed(0)
maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)

input()
"""
#circle
"""
for i in range (0,360):
    maTortue.forward(1)
    maTortue.left(1)
    maTortue.speed(0)

input()
"""
#square snail 
"""
distance = 5

for i in range(2000):
    maTortue.speed(0)
    maTortue.forward(distance)
    maTortue.left(90)
    distance+=2

input()
"""
#spirale infinie
'''
for i in range (0,3600):
    maTortue.forward(1+i/360)
    maTortue.left(1)

input()
'''
#marche aléatoire

def pas(maTortue):
    aleatoire = random.randint(0, 3)

    if aleatoire == 1:
        maTortue.left(90)
        maTortue.forward(4)
    elif aleatoire == 2:
        maTortue.right(90)
        maTortue.forward(4)
    else :
        maTortue.forward(3)


def marcheAleatoire(maTortue):
    while 1 :
        pas(maTortue)

#marcheAleatoire(maTortue)

#initialisation de la couleur
T1=turtle.Turtle()
T2=turtle.Turtle()
T3=turtle.Turtle()
T4=turtle.Turtle()
T1.color("purple")
T1.shape("turtle")
T2.color("lightblue")
T2.shape("turtle")
T3.color("grey")
T3.shape("turtle")
T4.color("pink")
T4.shape("turtle")

#positions aleatoires des tortues
T1.penup()
T1.goto(random.randint(-100,100),random.randint(-100,100))
T1.pendown()
T2.penup()
T2.goto(random.randint(-100,100),random.randint(-100,100))
T2.pendown()
T3.penup()
T3.goto(random.randint(-100,100),random.randint(-100,100))
T3.pendown()


def marcheATrois(Tortue1,Tortue2,Tortue3,Tortue4):
    while 1 : 
        pas(Tortue1)
        pas(Tortue2)
        pas(Tortue3)
        pas(Tortue4)


marcheATrois(T1,T2,T3,T4)

#input()


