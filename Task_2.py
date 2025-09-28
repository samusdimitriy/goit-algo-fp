import turtle


def draw_tree(t, length, angle, level):
    if level == 0:
        return

    t.width(level)
    t.color("brown" if level > 3 else "green")

    t.forward(length)

    if level > 1:
        t.left(angle)
        draw_tree(t, length * 0.7, angle, level - 1)

        t.right(2 * angle)
        draw_tree(t, length * 0.7, angle, level - 1)

        t.left(angle)

    t.backward(length)


def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.setup(800, 600)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    level_input = turtle.textinput("Pythagoras Tree", "Enter recursion level (1-10):")
    level = int(level_input) if level_input and level_input.isdigit() else 7
    level = max(1, min(level, 10))

    draw_tree(t, 120, 30, level)

    screen.exitonclick()


if __name__ == "__main__":
    main()
