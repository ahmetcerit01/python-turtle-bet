import turtle
from turtle import Screen,Turtle

my_turtle = Turtle()
screen = Screen()

my_turtle.color("green")
my_turtle.pensize(3)
def move_forward():
    my_turtle.forward(10)
def move_back():
    my_turtle.back(10)

def turn_right():
    my_turtle.right(10)

def turn_left():
    my_turtle.left(10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()

screen.onkeypress(key="w",fun=move_forward) # böyle yaparak da basılı tutarak etkinleştirebiliriz.
screen.onkey(key="s",fun=move_back)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
