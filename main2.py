from turtle import *

window = Screen()
#Pen()
reset()
shape("turtle")
bgcolor("red")
color("white")
liczba_powtorzen = 18

speed(100)
pensize(3)
for i in range(liczba_powtorzen):
    circle(80*i)
    left(20)

window.exitonclick()
