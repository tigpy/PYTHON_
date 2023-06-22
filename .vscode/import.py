import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(5)

# Define function to draw a filled polygon
def draw_filled_polygon(sides, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)
    t.end_fill()

# Draw outer rectangle
t.penup()
t.goto(-200, -100)
t.pendown()
draw_filled_polygon(4, 400, "red")

# Draw inner rectangle
t.penup()
t.goto(-140, -60)
t.pendown()
draw_filled_polygon(4, 280, "white")

# Draw left triangle
t.penup()
t.goto(-200, 0)
t.pendown()
draw_filled_polygon(3, 80, "blue")

# Draw right triangle
t.penup()
t.goto(120, 0)
t.pendown()
draw_filled_polygon(3, 80, "blue")

# Draw upper left circle
t.penup()
t.goto(-180, 40)
t.pendown()
t.circle(40)

# Draw upper right circle
t.penup()
t.goto(100, 40)
t.pendown()
t.circle(40)

# Draw lower left circle
t.penup()
t.goto(-180, -40)
t.pendown()
t.circle(40)

# Draw lower right circle
t.penup()
t.goto(100, -40)
t.pendown()
t.circle(40)

# Hide turtle
t.hideturtle()

# Keep window open until user closes it
turtle.mainloop()

