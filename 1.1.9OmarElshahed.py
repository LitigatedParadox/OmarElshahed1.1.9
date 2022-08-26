import turtle as trtl
import random
from playsound import playsound
import os

x = -1000

G = 'G.ogg'
A = 'A.ogg'
B = 'B.ogg'
C = 'C.ogg'
D = 'D.ogg'
E = 'E.ogg'
F = 'F.ogg'
High_G = 'High_G.ogg'
High_A = 'High_A.ogg'
CWD = os.getcwd()

Pitches = []

Melody = []

def goto_make_circle(Y):
    trtl.penup()
    trtl.goto(x, Y)
    trtl.pendown
    trtl.color("black")
    trtl.fillcolor("black")
    trtl.begin_fill()
    trtl.circle(2)
    trtl.end_fill()

#def PlayNote(FileName):
#    AudioPath = os.getcwd()
#    playsound(f'{AudioPath}\\{FileName}')
#   Melody.append(FileName)


Staff_Lines_Y = [-100, -50, 0, 50, 100]
Measures_X = [-500, 0, 500]


#Iterates through the list of Y values that each line will start at.
for Y_Pos in Staff_Lines_Y:
    trtl.penup()
    trtl.goto(-1000, Y_Pos)
    trtl.pendown()
    trtl.forward(2000)

for Measure in Measures_X:
    trtl.penup()
    trtl.goto(Measure, 100)
    trtl.right(90)
    trtl.pendown()
    trtl.forward(200)
    trtl.left(90)


trtl.penup()
trtl.goto(0, 100)
trtl.right(90)
trtl.pendown()
trtl.forward(200)

for i in range(8):
    x += 200
    n = random.randint(0, 9)
    if n < 1:
        goto_make_circle(-100)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\G.ogg')
    elif n < 2:
        goto_make_circle(-50)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\B.ogg')
    elif n < 3:
        goto_make_circle(0)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\D.ogg')
    elif n < 4:
        goto_make_circle(50)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\F.ogg')
    elif n < 5:
        goto_make_circle(100)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\High_A.ogg')
    elif n < 6:
        goto_make_circle(-75)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\A.ogg')
    elif n < 7:
        goto_make_circle(-25)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\C.ogg')
    elif n < 8:
        goto_make_circle(25)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\E.ogg')
    elif n < 9:
        goto_make_circle(75)
        playsound('C:\\Users\\Shahed\\Downloads\\School Downloads\\CSP\\High_G.ogg')

wn = trtl.Screen()
wn.mainloop()