import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Bandeira do Brasil")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()

def retangulo(x, y, largura, altura, cor):
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.left(90)
        t.forward(altura)
        t.left(90)
    t.end_fill()
    t.penup()

def losango(cx, cy, dx, dy, cor):
    t.goto(cx, cy + dy)
    t.pendown()
    t.color(cor)
    t.begin_fill()
    t.goto(cx + dx, cy)
    t.goto(cx, cy - dy)
    t.goto(cx - dx, cy)
    t.goto(cx, cy + dy)
    t.end_fill()
    t.penup()

def circulo(cx, cy, r, cor):
    t.goto(cx, cy - r)
    t.pendown()
    t.color(cor)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

retangulo(-400, -300, 800, 600, "#009C3B")
losango(0, 0, 340, 210, "#FFDF00")
circulo(0, 0, 130, "#002776")

t.goto(-125, -12)
t.pendown()
t.color("white")
t.begin_fill()
t.goto(125, -12)
t.goto(125, 12)
t.goto(-125, 12)
t.goto(-125, -12)
t.end_fill()
t.penup()

t.goto(0, -9)
t.color("#002776")
t.write("ORDEM E PROGRESSO", align="center", font=("Arial", 9, "bold"))

for x, y in [(-60, 30), (-30, 55), (10, 40), (50, 60), (80, 30),
             (60, -10), (30, -40), (-10, -50), (-50, -30), (-80, 10)]:
    t.goto(x, y)
    t.color("white")
    t.dot(6)

screen.update()
screen.exitonclick()
