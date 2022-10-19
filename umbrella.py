from turtle import *
speed(100)
colors = ['black', 'red']
bgcolor('white')

for i in range(1000):
    pencolor(colors[i%2])
    width(i//100+1)
   
    for t in range(1000):
        forward(i-t+2)
        left(i-t+1)
done