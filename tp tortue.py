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
def spirale:
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
    pas(maTortue)

#marcheAleatoire(maTortue)
def marcheATrois(liste):
    for i in liste:
        pas(i)

liste=[]
n=4
for i in range(n):
    liste.append(turtle.Turtle())
    
for i in liste:
    i.penup()
    i.goto(random.randint(-100,100),random.randint(-100,100))
    i.pendown()
    i.color(random.random(),random.random(),random.random())
    i.shape("turtle")

while 1:
    marcheATrois(liste)
    marcheAleatoire(maTortue)
    

input()


