from turtle import *

# A function is defined for each part, with the following steps
#    1. pen up
#    2. move to correct position
#    3. pen down
#    4. draw
#    5. return home

class Face:

    def __init__(self, xpos, ypos):
       self.size = 90
       self.coord = (xpos, ypos)
       self.nosesize = 'small'
    
    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)

def goHome(self):
    penup()
    goto(self.coord)

    setheading(0)

def drawOutline(self):
    penup()
    forward(self.size)
    left(90)

    pendown()
    circle(self.size)
    self.gohome
        
def drawEye(self, turn):
    penup()
    left(turn)
    forward(self.size / 2)
    pendown()
    dot(self.size/10)
    self.gohome()

def drawMouth(self):
    penup()
    right(135)
    forward(self.size/1.7)
    left(90)
    pendown()
    circle(self.size/1.7,90)
    self.gohome()

    def drawNose(self):
        if self.nosesize == 'large' :
            dot(self.size/2)