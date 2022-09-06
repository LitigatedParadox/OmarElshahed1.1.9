#a121_catch_a_turtle.py
#-----import statements-----
import random as rand
import turtle as trtl
import time
import leaderboard as lb
LeaderboardText = open("leaderboard.txt", "r")
trtl.speed(0)
#-----game configuration-----
TrtlColor = "pink"
TrtlSize = 2
TrtlShape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000 #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
Spot = trtl
Spot.shape(TrtlShape)
Spot.shapesize(TrtlSize)
Spot.color(TrtlColor)
score_writer = trtl.Turtle()
score_writer.pencolor("black")
score_writer.hideturtle()
score_writer.speed(0)
counter = trtl.Turtle()
#-----game functions-----
PlayerName = input("Enter your name: ")
score_writer.penup()
score_writer.goto(-800, 400)
def change_position():
    x = rand.randint(-1000, 1000)
    y = rand.randint(-500, 500)
    Spot.penup()
    Spot.goto(x, y)
    Spot.pendown()

def spot_clicked(x, y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        counter.hideturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
    global timer, timer_up
    counter.penup()
    counter.hideturtle()
    counter.goto(800, 400)
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up=True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen()
        counter.ontimer(countdown, counter_interval)

#-----events----------------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(LeaderboardText)
  leader_scores_list = lb.get_scores(LeaderboardText)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(LeaderboardText, leader_names_list, leader_scores_list, PlayerName, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
Spot.onclick(spot_clicked)
wn=Spot.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()