from turtle import *
speed(100)
colors = ['black', 'red', 'black', 'red']
bgcolor('white')

for i in range(1000):
    pencolor(colors[i%4])
    width(i//100+1)
    forward(i)
    left(9999)
done