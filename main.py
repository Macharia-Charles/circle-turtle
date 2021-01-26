import turtle
globals()
mash_turtle = turtle.Turtle()


def draw_square(length, angle):
    for turn in range(4):
        mash_turtle.speed(5)
        mash_turtle.forward(length)
        mash_turtle.right(angle)


for i in range(37):
    draw_square(100, 90)
    mash_turtle.right(10)
