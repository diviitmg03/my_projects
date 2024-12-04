import turtle
import random
import time
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("OGGY AND THE COCKROACHES")
wn.setup(800, 800)

score = 0
lives = 3
temp_pen = turtle.Turtle()
temp_pen.speed(0)
temp_pen.color('white')
temp_pen.penup()
temp_pen.goto(0, 350)
temp_pen.pendown()
temp_pen.write('SCORE:{}    LIVES:{}'.format(score, lives), font=('Courier', 24, ''), align='center')

temp_pen.hideturtle()


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.up()
        self.speed(10)


class Oggy(turtle.Turtle):
    def __init__(self, w, d):
        self.w = w
        self.d = d
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color('cyan')
        self.penup()
        self.speed(1)

    def moveLeft(self):
        self.d = 'left'

    def moveRight(self):
        self.d = 'right'

    def moveUp(self):
        self.d = 'up'

    def moveDown(self):
        self.d = 'down'

    def movement(self):

        if self.d == 'left':
            x = oggy.xcor() - 20
            y = oggy.ycor()
            if (x, y) not in self.w:
                oggy.goto((x, y))

        if self.d == 'right':
            x = oggy.xcor() + 20
            y = oggy.ycor()
            if (x, y) not in self.w:
                oggy.goto((x, y))

        if self.d == 'up':
            y = oggy.ycor() + 20
            x = oggy.xcor()
            if (x, y) not in self.w:
                oggy.goto((x, y))

        if self.d == 'down':
            y = oggy.ycor() - 20
            x = oggy.xcor()
            if (x, y) not in self.w:
                oggy.goto((x, y))


level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XO    XXXX   P      PXXXXXXXXX",
    "X  XX XXXX XXXXXXX X       DXX",
    "X  XXDXXXX XXXXXXXPXXXXXXX  XX",
    "X      PXX XXX         XXXM XX",
    "X XXXX XXX XXX XXXXXXXXXXX  XX",
    "X    XDXXX XXX XXXP XXXXXX JXX",
    "XXXX X XXX X  PXXXM         XX",
    "X PX X        XXXX  XXXXXX  XX",
    "X  X X JXXXXXXXXXXXXXXXXXXXXXX",
    "X          P                PX",
    "XX XXX XXXXXXXXXXXXXXXXXXX X X",
    "X P              XXXXX  XX X X",
    "X XXXX XXXX XXX JXXXXX  XX  PX",
    "X X PX XXXX XXX         XXX  X",
    "X      D                XPX  X",
    "X XXXXXXXXPXXXXXXXXXXXXXX    X",
    "X       XX XXX P     PXXX XX X",
    "XXXXXXX XX XXX XXXXXX    PXX X",
    "XX PXXX XX P        P    XXX X",
    "XX  D   XXXXX XXXX  XXXX XXX X",
    "XX XXXX XXXXX    X  XXXX XXX X",
    "X    P      X DX     P    M  X",
    "X XXXXXXXXXXX  X XXXXX XXXX XX",
    "X XX  P  MXXXD X     X   PX  X",
    "X XX XXXX X   P X XX  PXX XX X",
    "X XX XXXX X  XXJX MX XXXXPXX X",
    "X J P     XX XX XX X   M  XX X",
    "XPXXX XXX     P  XX   XXXX  PX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

pen = Pen()


def walls():
    wall = []
    for i in range(len(level_1)):
        for j in range(len(level_1[i])):
            screen_x = -300 + (j * 20)
            screen_y = 300 - (i * 20)
            if level_1[i][j] == 'X':
                wall.append((screen_x, screen_y))

    return wall


w = walls()
direction = 'stop'

oggy = Oggy(w, direction)

points = []
cockroaches = []

path = []
def create_game():
    for i in range(len(level_1)):
        for j in range(len(level_1[i])):
            c = level_1[i][j]

            screen_x = -300 + (j * 20)
            screen_y = 300 - (i * 20)

            if c == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if c == 'O':
                oggy.goto(screen_x, screen_y)
            if c == 'D':
                dee = turtle.Turtle()
                dee.speed(10)
                dee.color('red')
                dee.shape('turtle')
                dee.penup()
                dee.shapesize(stretch_wid=0.8, stretch_len=0.8)
                dee.goto((screen_x, screen_y))
                cockroaches.append(dee)

            if c == 'J':
                joey = turtle.Turtle()
                joey.speed(10)
                joey.color('purple')
                joey.shape('turtle')
                joey.penup()
                joey.shapesize(stretch_wid=0.8, stretch_len=0.8)
                joey.goto((screen_x, screen_y))
                cockroaches.append(joey)

            if c == 'M':
                marky = turtle.Turtle()
                marky.speed(10)
                marky.color('dark green')
                marky.shape('turtle')
                marky.penup()
                marky.shapesize(stretch_wid=0.8, stretch_len=0.8)
                marky.goto((screen_x, screen_y))
                cockroaches.append(marky)

            if c == 'P':
                point = turtle.Turtle()
                point.speed(10)
                point.color('yellow')
                point.shape('circle')
                point.shapesize(stretch_wid=0.4, stretch_len=0.4)
                point.penup()
                point.goto((screen_x, screen_y))
                points.append(point)

            if c == ' ':
                path.append((screen_x, screen_y))


create_game()


# def move(cock, w):
#     l_c = []
#     p_r = (cock.xcor() + 20, cock.ycor())
#     p_l = (cock.xcor() - 20, cock.ycor())
#     p_u = (cock.xcor(), cock.ycor() + 20)
#     p_d = (cock.xcor(), cock.ycor() - 20)
#     l = [p_r, p_l, p_u, p_d]
#     for i in l:
#         if i not in w:
#             l_c.append(i)
#     n_p = random.choice(l)
#
#     cock.goto(n_p)


wn.listen()

wn.onkeypress(oggy.moveLeft, 'Left')
wn.onkeypress(oggy.moveRight, 'Right')
wn.onkeypress(oggy.moveUp, 'Up')
wn.onkeypress(oggy.moveDown, 'Down')

restart= 0
while True:
    wn.update()
    oggy.movement()
    # move(dee, walls())
    # move(joey, walls())
    # move(marky, walls())

    for point in points:
        if oggy.pos() == point.pos() and lives > 0:
            # point.hideturtle()
            spawn_loc = random.choice(path)
            point.goto(spawn_loc)

            temp_pen.clear()
            score += 1
            temp_pen.write('SCORE:{}    LIVES:{}'.format(score, lives), font=('Courier', 24, ''), align='center')

    for cockroach in cockroaches:
        if oggy.pos() == cockroach.pos() and lives > 0:
            temp_pen.clear()
            lives -= 1
            temp_pen.write('SCORE:{}    LIVES:{}'.format(score, lives), font=('Courier', 24, ''), align='center')
            time.sleep(1)
    if lives == 0 and restart == 0:
        temp_pen.clear()
        temp_pen.write('SCORE:{}'.format(score), font=('Courier', 24, ''), align='center')
        temp_pen.clear()

        temp_pen.write('GAME OVER!', font=('Courier', 48, ''), align='center')
        time.sleep(2)

        restart = 1

    if restart == 1:
        score = 0
        lives = 3

        temp_pen.clear()
        temp_pen.write('RESETTING GAME!', font=('Courier', 48, ''), align='center')
        create_game()
        temp_pen.clear()
        temp_pen.write('SCORE:{}    LIVES:{}'.format(score, lives), font=('Courier', 24, ''), align='center')

        restart = 0