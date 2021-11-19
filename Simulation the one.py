import random
import time
import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 5555

print('waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)

class sim:

 def matchStart(self):

     # Players have Pace, Shoot
     #ramos = ["Ramos", 71, 70]
     #pique = ["Pique", 57, 61]
     #ronaldo = ["Ronaldo", 87, 93]

     #bale = ["Bale", 91, 87]
     #hazard = ["Hazard", 89, 81]
     #aguero = ["Aguero", 78, 90]

     my_team_score = 0  # user team score
     opp_team_score = 0  # opposing team score
     match_time = 0 # match time to control when the game should end
     t = 6 # rounds

     game_on = "The whistle is blowed and the game is on! "
     player_are = 'is headed for the ball!'
     got_ball = 'got the ball!'
     no_ball = 'failed to get the ball! embarrassing!'
     shoot_text = 'uses all his power and shoots!'
     goal = 'have scored a goal! what a fantastic goal indeed!'
     no_goal = "missed the goal! what a fail!"
     win = "The game is over and the winner is: "
     scores = "The score is: "
     tie = "The game is over! and is a strong tie!"
     on_again = "The game is back on again!"

     # players team
     my_team = [ramos, pique, ronaldo]
     # opposing team
     opposing_team = [bale, hazard, aguero]

     print(game_on) # game starts
     time.sleep(2)
     while match_time <= t:
         rs = random.choice(my_team + opposing_team)  # picks a random player from both teams
         r_ball = random.randint(0, 100)  # random pace vaule
         r_shoot = random.randint(0, 100)  # random shoot vaule
         print(rs[0], player_are)  # headed for the ball
         time.sleep(2)
         if rs[1] >= r_ball: # if the players pace are >= the random pace, the player gets the ball
             print(rs[0], got_ball)  # got the ball
             time.sleep(2)
             print(rs[0], shoot_text)
             time.sleep(1)
             if rs[2] >= r_shoot:  # if the players shoot val are >= the random shoot val, the player gets a goal
                 match_time +=1
                 time.sleep(2)
                 print(rs[0], goal)  # there are goal
                 time.sleep(2)
                 if rs in my_team:
                     my_team_score += 1
                     print(scores)
                     print(f"My team: {my_team_score}")
                     print(f"opposing team: {opp_team_score}")
                     time.sleep(3)
                     if match_time == t:
                         break
                     print(on_again)
                     time.sleep(2)
                 else:
                     opp_team_score += 1
                     print(scores)
                     print(f"My team: {my_team_score}")
                     print(f"opposing team: {opp_team_score}")
                     time.sleep(3)
                     if match_time == t:
                         break
                     print(on_again)
                     time.sleep(2)
             else:
                 print(rs[0], no_goal)  # no goal
                 time.sleep(2)
         else:
             print(rs[0],no_ball)
             time.sleep(2)

     if my_team_score > opp_team_score: # if user team wins
         print(win, "My team !....what a game!")
     elif my_team_score < opp_team_score: # if the opposing team wins
         print(win, "The opposing team ! better luck next time champ")
     else:
         print(tie)  # if it's a tie
         print(f"My team: {my_team_score}")
         print(f"opposing team: {opp_team_score}")

     time.sleep(3)
sim.matchStart(self=sim)