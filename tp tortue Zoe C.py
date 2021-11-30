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
'''
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
'''
#Exercice agar.io

import turtle
import random
turtle.speed(0)
turtle.delay(0)
#maTortue=turtle.Turtle()
size=3
turtle.penup()
turtle.shapesize(size)
turtle.shape("turtle")
turtle.color("pink")

def gauche (tortue):
    tortue.left(90)
def droite (tortue):
    tortue.right(90)

def listortue (n):
    liste=[]
    for i in range (0,n):
        liste.append(turtle.Turtle())
    return liste

def placr ():
    for tortue in listofT:
        tortue.penup()
        tortue.color(random.random(),random.random(),random.random())
        tortue.shape("turtle")
        tortue.goto(random.randint(-300,300),random.randint(-300,300))

def maral (tortue):
    test = random.randint(1,3)
    if test == 1:
        gauche(tortue)
        tortue.forward(5)
    elif test ==2:
        droite(tortue)
        tortue.forward(5)
    else:
        tortue.forward(10)


def changeUpPosition():
    turtle.setheading(90)
def changeRightPosition():
    turtle.setheading(0)
def changeLeftPosition():
    turtle.setheading(180)
def changeDownPosition():
    turtle.setheading(270)

turtle.onkeypress(changeUpPosition,"Up")
turtle.onkeypress(changeLeftPosition,"Left")
turtle.onkeypress(changeRightPosition,"Right")
turtle.onkeypress(changeDownPosition,"Down")
turtle.listen()

cpt=0
n=20
listofT=listortue(n)
placr()
cel=1

while 1:
    turtle.speed(1)
    turtle.forward(cel)
    print(turtle.distance(listofT[0]))
    if cpt%10==0:
        for i in listofT:
            maral(i)

    for i in listofT:
        if turtle.distance(i) < size*7 :
            i.hideturtle()
            listofT.remove(i)
            size +=0.5
            turtle.shapesize(size)
            cel=cel*0.9
    cpt+=1



input()
