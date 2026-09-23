import turtle
import datetime

sc = turtle.Screen()
sc.setup(620, 520)
sc.title("Reloj")
sc.bgcolor("#D0D0D0")
sc.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

b = turtle.Turtle()
b.hideturtle()
b.speed(0)

rodando = True

def desenhar_relogio():
    t.penup()
    t.goto(0, -120)
    t.setheading(0)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    t.circle(150)
    t.end_fill()
    t.penup()

    for i in range(60):
        t.goto(0, 30)
        t.setheading(90 - i * 6)
        if i % 5 == 0:
            t.pensize(3)
            t.forward(130)
            t.pendown()
            t.forward(20)
        else:
            t.pensize(1)
            t.forward(140)
            t.pendown()
            t.forward(10)
        t.penup()

def ponteiro(angulo, tam, cor, esp):
    t.goto(0, 30)
    t.setheading(90 - angulo)
    t.pensize(esp)
    t.pencolor(cor)
    t.pendown()
    t.forward(tam)
    t.penup()

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

def update():
    t.clear()
    now = datetime.datetime.now()

    desenhar_relogio()

    t.goto(0, 85)
    t.pencolor("black")
    t.write(dias[now.weekday()], align="center", font=("Arial", 13, "bold"))

    t.goto(0, -15)
    t.write(meses[now.month-1] + ". " + str(now.day) + " " + str(now.year),
            align="center", font=("Arial", 11, "normal"))

    ponteiro(now.second * 6, 130, "red", 1)
    ponteiro(now.minute * 6 + now.second * 0.1, 100, "#003399", 3)
    ponteiro((now.hour % 12) * 30 + now.minute * 0.5, 70, "#003399", 5)

    t.goto(0, 30)
    t.dot(8, "black")

    sc.update()

    if rodando:
        sc.ontimer(update, 1000)

# botao stop
b.penup()
b.goto(-55, -215)
b.pendown()
b.color("#880000", "#CC0000")
b.begin_fill()
for _ in range(2):
    b.forward(110)
    b.left(90)
    b.forward(35)
    b.left(90)
b.end_fill()
b.penup()
b.goto(0, -210)
b.pencolor("white")
b.write("STOP", align="center", font=("Arial", 13, "bold"))

def clic(x, y):
    global rodando
    if -55 < x < 55 and -215 < y < -180:
        rodando = False
        b.clear()
        b.goto(0, -205)
        b.pencolor("black")
        b.write("Detenido.", align="center", font=("Arial", 12, "bold"))
        sc.update()

sc.onclick(clic)
update()
sc.mainloop()