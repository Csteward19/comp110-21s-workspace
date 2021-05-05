from turtle import Turtle, done


TRUNK = 100.0
UP = 90.0

t: Turtle = Turtle()


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, UP)

def branch(length: float, angle: float)-> None:
    t.setheading(angle + 180.0)
    t.forward(length)


if __name__ == "__main__":
    t.speed(5)
    tree(0, 0)
    done()