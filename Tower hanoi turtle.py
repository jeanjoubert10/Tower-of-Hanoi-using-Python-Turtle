
import turtle
import time

win = turtle.Screen()
win.setup(800,600)
win.title('Tower of Hanoi')
win.tracer(0)


base = turtle.Turtle()
base.color('grey')
base.shape('square')
base.up()
base.goto(0,-200)
base.shapesize(1,35)

class Pin(turtle.Turtle):
    def __init__(self, xpos):
        super().__init__(shape='square')
        self.xpos = xpos
        self.up()
        self.color('grey')
        self.shapesize(10,1)
        self.goto(self.xpos,-100)
        self.count = 0
        self.pos_list = [-180, -160, -140, -120, -100]
        self.discs = []


class Disc(turtle.Turtle):
    def __init__(self, xpos, ypos, size, color):
        super().__init__(shape='square')
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.color(color)
        self.up()
        self.shapesize(1,self.size)
        self.goto(self.xpos,self.ypos)

def move_disc(disc, pin):
    while disc.ycor()<100:
        disc.goto(disc.xcor(),disc.ycor()+2)
        win.update()
    disc.goto(pin.xcor(),100)
    win.update()
    while disc.ycor()>pin.pos_list[pin.count]:
        disc.goto(disc.xcor(),disc.ycor()-2)
        win.update()
    #pin.count+= 1

def move(f,t):
    print(f'Move disc from {f} to {t}!')
    if f == 'A':
        top_disc = pin1.discs[-1]
        start_pin = pin1
    elif f == 'B':
        top_disc = pin2.discs[-1]
        start_pin = pin2
    elif f == 'C':
        top_disc = pin3.discs[-1]
        start_pin = pin3

    if t == 'A':
        pin = pin1
    elif t == 'B':
        pin = pin2
    elif t == 'C':
        pin = pin3
        
    move_disc(top_disc,pin)
    start_pin.count-=1
    start_pin.discs.pop()
    pin.count+=1
    pin.discs.append(top_disc)

def moveVia(f,v,t):
    move(f,v)
    move(v,t)

# n number of discs
# f from position, h helper(via) and target
def hanoi(n,f,h,t):
    if n == 0:  # Prevent from moving 0 or negative discs
        pass
    else:
        hanoi(n-1,f,t,h) # move all but bottom to helper (A to B using C)
        move(f,t) # move bottom disc to target (from A to C)
        hanoi(n-1,h,f,t) # move rest from helper to target via from (from B to C using A)
        
pin1 = Pin(-200)
pin2 = Pin(0)
pin3 = Pin(200)

disc1 = Disc(-200, -180, 10, 'orange')
disc2 = Disc(-200, -160, 8, 'blue')
disc3 = Disc(-200, -140, 6, 'red')
disc4 = Disc(-200, -120, 4, 'yellow')
disc5 = Disc(-200, -100, 2, 'green')

pin1.count=5
pin1.discs = [disc1,disc2,disc3,disc4,disc5]
time.sleep(10)
hanoi(5, 'A', 'B', 'C')
