import turtle as trtl
import random
from playsound import playsound
import time

trtl.hideturtle()
x = -1125

G = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\G.wav'
A = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\A.wav'
B = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\B.wav'
C = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\C.wav'
D = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\D.wav'
E = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\E.wav'
F = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\F.wav'
High_G = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\High_G.wav'
High_A = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\High_A.wav'



def goto_make_circle(Y):
    trtl.penup()
    trtl.goto(x, Y)
    trtl.pendown
    trtl.color("black")
    trtl.fillcolor("black")
    trtl.begin_fill()
    trtl.circle(25)
    trtl.end_fill()

#def PlayNote(FileName):
#    AudioPath = os.getcwd()
#    playsound(f'{AudioPath}\{FileName}')
#   Melody.append(FileName)


Staff_Lines_Y = [-100, -50, 0, 50, 100]
Measures_X = [-500, 0, 500]
Melody = []

Command = input("For those of you who are perturbed by the lack of time signature, key, clef etc. don't worry! Those are all just off the screen. I definitely didn't omit those because they would be too hard to program! ")


if Command == "Sudo secret":
    playsound(r'C:\Users\Shahed\youtube-dl\Among Us Drip Theme Song Original (Among Us Trap Remix _ Amogus Meme Music)-grd-K33tOSM.wav')
else:
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
        x += 250
        n = random.randint(0, 9)
        if n < 1:
            goto_make_circle(-100)
            playsound(G)
            Melody.append(G)
        elif n < 2:
            goto_make_circle(-50)
            playsound(B)
            Melody.append(B)
        elif n < 3:
            goto_make_circle(0)
            playsound(D)
            Melody.append(D)
        elif n < 4:
            goto_make_circle(50)
            playsound(F)
            Melody.append(F)
        elif n < 5:
            goto_make_circle(100)
            playsound(High_A)
            Melody.append(High_A)
        elif n < 6:
            goto_make_circle(-75)
            playsound(A)
            Melody.append(A)
        elif n < 7:
            goto_make_circle(-25)
            playsound(C)
            Melody.append(C)
        elif n < 8:
            goto_make_circle(25)
            playsound(E)
            Melody.append(E)
        elif n < 9:
            goto_make_circle(75)
            playsound(High_G)
            Melody.append(High_G)

time.sleep(2)
print(Melody)

for note in Melody:
    playsound(note)

    wn = trtl.Screen()
    wn.mainloop()