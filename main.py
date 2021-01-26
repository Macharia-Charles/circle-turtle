import turtle
globals()
mash_turtle = turtle.Turtle()


def draw_square():
    mash_turtle.speed(5)
    mash_turtle.forward(100)
    mash_turtle.right(90)
    mash_turtle.forward(100)
    mash_turtle.right(90)
    mash_turtle.forward(100)
    mash_turtle.right(90)
    mash_turtle.forward(100)


for i in range(36):
    draw_square()
    mash_turtle.right(100)
