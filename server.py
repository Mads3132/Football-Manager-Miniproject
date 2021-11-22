import socket
from _thread import *
import random
import time
import pickle

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 5555
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for incoming connection(s)...')
ServerSocket.listen(3)

def threaded_client(connection):
    idkman = 1
    connection.send(str.encode('Welcome to the server'))
    while True:
        data = connection.recv(1024)
        unpickled_my_team = pickle.loads(data)
        print(unpickled_my_team)

        if idkman == 1:
            class sim:

                def matchStart(self):

                    # Players have Pace, Shoot
                    ramos = ["Ramos", 71, 70]
                    pique = ["Pique", 57, 61]
                    ronaldo = ["Ronaldo", 87, 93]

                    messi = ["Messi", 50, 87, 92]
                    hart = ["Hart", 20, 58, 64]
                    curtois = ["Curtois", 18, 52, 74]
                    navas = ["Navas", 20, 54, 75]
                    bravo = ["Bravo", 15, 59, 86]
                    cech = ["Cech", 15, 51, 79]
                    de_gea = ["De Gea", 20, 50, 78]
                    ramos = ["Ramos", 40, 71, 70]
                    pique = ["Pique", 30, 57, 61]
                    ronaldo = ["Ronaldo", 50, 87, 93]
                    suarez = ["Suarez", 45, 72, 90]

                    my_team_score = 0  # user team score
                    opp_team_score = 0  # opposing team score
                    match_time = 0  # match time to control when the game should end
                    t = 3  # rounds

                    game_on = "The whistle is blowed and the game is on! "
                    player_are = 'is headed for the ball!'
                    got_ball = 'got the ball!'
                    no_ball = 'failed to get the ball! embarrassing!'
                    shoot_text = 'uses all his power and shoots!'
                    goal = 'have scored a goal! what a fantasisk goal indeed!'
                    no_goal = "missed the goal! what a fail!"
                    win = "The game is over and the winner is: "
                    scores = "The score is: "
                    tie = "The game is over! and is a strong tie!"
                    on_again = "The game is back on again!"

                # players team
                    my_team = unpickled_my_team
                # opposing team
                    opposing_team = []

                    opposing_team.append(messi)
                    opposing_team.append(hart)
                    opposing_team.append(curtois)
                    opposing_team.append(navas)
                    opposing_team.append(bravo)
                    opposing_team.append(cech)
                    opposing_team.append(de_gea)
                    opposing_team.append(ramos)
                    opposing_team.append(pique)
                    opposing_team.append(ronaldo)
                    opposing_team.append(suarez)

                    print(game_on)  # game starts
                    time.sleep(2)
                    while match_time <= t:
                        rs = random.choice(my_team + opposing_team)  # picks a random player from both teams
                        r_ball = random.randint(0, 100)  # random pace vaule
                        r_shoot = random.randint(0, 100)  # random shoot vaule
                        print(rs[0], player_are)  # headed for the ball
                        time.sleep(2)
                        if rs[1] >= r_ball:  # if the players pace are >= the random pace, the player gets the ball
                            print(rs[0], got_ball)  # got the ball
                            time.sleep(2)
                            print(rs[0], shoot_text)
                            time.sleep(1)
                            if rs[2] >= r_shoot:  # if the players shoot val are >= the random shoot val, the player gets a goal
                                match_time += 1
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
                            print(rs[0], no_ball)
                            time.sleep(2)

                    if my_team_score > opp_team_score:  # if user team wins
                        print(win, "My team !....what a game!")
                    elif my_team_score < opp_team_score:  # if the opposing team wins
                        print(win, "The opposing team ! better luck next time champ")
                    else:
                        print(tie)  # if it's a tie


                    time.sleep(3)
            idkman = 2

            sim.matchStart(self=sim)

        if not data:
            break
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount +=1
    print('Thread number: ' + str(ThreadCount))
ServerSocket.close()