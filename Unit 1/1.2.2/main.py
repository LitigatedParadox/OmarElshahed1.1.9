#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
fruit = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(fruit) # Make the screen aware of the new file
wn.bgpic("background.gif")
#Initialize turtles. "apple" refers to the turtle that will fall from the tree, "letter" refers to the turtle that will write out letters
apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()
letter = trtl.Turtle()
letter.penup()
letter.goto(0,150)
apples_list = [apple1, apple2, apple3, apple4, apple5]
x = -250
y = 0
for apple in apples_list:
  apple.shape(fruit)
  apple.penup()
  apple.goto(x,y)
  x = x + 100


#----Randomization Set Up----
letters = ["a", "b", "c", "d", "e"]
def PickLetter():
  global letter_picked
  letter_picked = rand.choice(letters)
  l_index = int(letters.index(letter_picked))
  print(l_index)
  selected_apple = apples_list[l_index]
  print(selected_apple)
  letters.remove(letter_picked)



#Setup for initial natures of apples

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def Fruit_Falla():
#Fruit starts at (0, 0)
  apple1.right(90)
  apple1.forward(200)
  letter.hideturtle()
  apple1.clear()
  letter.clear()
  PickLetter()
  display_letter(letter_picked)

def Fruit_Fallb():
#Fruit starts at (0, 0)
  apple2.right(90)
  apple2.forward(200)
  letter.hideturtle()
  apple2.clear()
  letter.clear()
  PickLetter()
  display_letter(letter_picked)

def Fruit_Fallc():
#Fruit starts at (0,0)
  apple3.right(90)
  apple3.forward(200)
  letter.hideturtle()
  apple3.clear()
  letter.clear()
  PickLetter()
  display_letter(letter_picked)

def Fruit_Falld():
#Fruit starts at (0, 0)
  apple4.right(90)
  apple4.forward(200)
  letter.hideturtle()
  apple4.clear()
  letter.clear()
  PickLetter()
  display_letter(letter_picked)

def Fruit_Falle():
#Fruit starts at (0, 0)
  apple5.right(90)
  apple5.forward(200)
  letter.hideturtle()
  apple5.clear()
  letter.clear()
  PickLetter()
  display_letter(letter_picked)  
    

def display_letter(letter_picked):
  letter.color("black")
  letter.write(letter_picked, font = ("Retro", 74, "bold"))






#-----function calls-----


#----Events----
PickLetter()
display_letter(letter_picked)

for i in range(5):
  wn.onkeypress(Fruit_Falla, "a")
  wn.onkeypress(Fruit_Fallb, "b")
  wn.onkeypress(Fruit_Fallc, "c")
  wn.onkeypress(Fruit_Falld, "d")
  wn.onkeypress(Fruit_Falle, "e")


wn.listen()
wn.mainloop()

