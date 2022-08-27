#Import necessary modules
import turtle as trtl
import random
from playsound import playsound
import time

#Hide turtle, set speed to 0, initialize x variable which will be used later
trtl.speed(0)
trtl.hideturtle()
x = -1125

#Assign location of audio files to variable to represent notes
G = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\G.wav'
A = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\A.wav'
B = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\B.wav'
C = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\C.wav'
D = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\D.wav'
E = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\E.wav'
F = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\F.wav'
High_G = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\High_G.wav'
High_A = r'C:\Users\Shahed\Downloads\School_Downloads\CSP\1.1.9\High_A.wav'


#Define goto_make_circle function and requires 1 positional argument "Y" to run 
def goto_make_circle(Y):
    trtl.penup()
    trtl.goto(x, Y)
    trtl.pendown
    trtl.color("black")
    trtl.fillcolor("black")
    trtl.begin_fill()
    trtl.circle(25)
    trtl.end_fill()

#Creates list of Y values for staff lines and X values for measures
Staff_Lines_Y = [-100, -50, 0, 50, 100]
Measures_X = [-500, 0, 500]
#Creates empty melody list that notes will be assigned to later
Melody = []

#Takes user input, "Sudo secret" will play a surprise, other inputs will make the script proceed normally
Command = input("For those of you who are perturbed by the lack of time signature, key, clef etc. don't worry! Those are all just off the screen. I definitely didn't omit those because they would be too hard to program! ")
if Command == "Sudo secret":
    playsound(r'C:\Users\Shahed\youtube-dl\Secret.wav')
else:
    #Iterates through the list of Y values that each line will start at.
    for Y_Pos in Staff_Lines_Y:
        trtl.penup()
        trtl.goto(-1000, Y_Pos)
        trtl.pendown()
        trtl.forward(2000)
    #Iterates through list of X values that define postitions of measures
    for Measure in Measures_X:
        trtl.penup()
        trtl.goto(Measure, 100)
        trtl.right(90)
        trtl.pendown()
        trtl.forward(200)
        trtl.left(90)

    #Generates randomized 8 note melody. Upon each iteration x will be increased by 250 and n will be selected once again from a random range of values 0-9. Each if/elif statement calls the goto_make_circle() function as well as playing a note then appending that note to the Melody list
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

    #Gives a two second delay before playing the full melody
    time.sleep(2)
    print(Melody)
    for note in Melody:
        playsound(note)
    
    #Keeps turtle screen running throughout script
    wn = trtl.Screen()
    wn.mainloop()