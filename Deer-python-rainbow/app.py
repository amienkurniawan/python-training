#python to draw Rainbow Benzeneu using Turtle Programming
import turtle
colors = ['red','blue','green','orange','yellow','brown']
t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    # warna dari garis
    t.pencolor(colors[x % 6])
    # lebar dari garis
    t.width(x/100+1)
    # jarak dari garis
    t.forward(x)
    # sudut putaran
    t.left(60)