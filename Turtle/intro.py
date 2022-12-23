import turtle

turtle.Canvas()
turtle.pencolor("green")
turtle.begin_fill()
turtle.fillcolor("green")
turtle.bgcolor("yellow")

a = 20
for j in range(20):
    for i in range(4):
        turtle.right(90)
        turtle.backward(a)
    a = a+20
turtle.mainloop()
