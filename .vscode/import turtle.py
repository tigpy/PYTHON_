import turtle

def draw_donut(radius, gap):
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set turtle speed to fastest

    # Draw outer circle
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

    # Draw inner circle
    t.penup()
    t.goto(0, -gap)
    t.pendown()
    t.circle(radius-gap)

    # Fill in the donut shape
    t.penup()
    t.goto(0, 0)
    t.begin_fill()
    t.circle(radius, steps=100)
    t.circle(radius-gap, steps=100)
    t.end_fill()

    # Hide the turtle
    t.hideturtle()

# Call the function with a radius of 100 and a gap of 40
draw_donut(100, 40)

# Keep the window open until the user closes it
turtle.mainloop()
