import colorama
from colorama import Fore
from colorama import Style

#Players has Price, Pace, Shoot
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
neymar = ["Neymar", 48, 91, 85]
bale = ["Bale", 45, 91, 87]
hazard = ["Hazard", 42, 89, 81]
aguero = ["Aguero", 40, 78, 90]
smith = ["Smith", 2, 65, 56]
johhny = ["Johhny", 4, 67, 53]
sunny = ["Sunny", 8, 67, 60]
patrick = ["Patrick", 5, 66, 57]
debian = ["Debian", 3, 61, 51]
shaggy = ["Shaggy", 5, 70, 60]
randy = ["Randy", 3, 60, 53]
karim = ["Karim", 6, 52, 60]
samuel = ["Samuel", 2, 54, 58]
billy = ["Billy", 4, 55, 59]
aaron = ["Aaron", 5, 60, 60]

#Collect all players in an array
players = []
players.append(messi)
players.append(hart)
players.append(curtois)
players.append(navas)
players.append(bravo)
players.append(cech)
players.append(de_gea)
players.append(ramos)
players.append(pique)
players.append(ronaldo)
players.append(suarez)
players.append(neymar)
players.append(bale)
players.append(hazard)
players.append(aguero)
players.append(smith)
players.append(johhny)
players.append(sunny)
players.append(patrick)
players.append(debian)
players.append(shaggy)
players.append(randy)
players.append(karim)
players.append(samuel)
players.append(billy)
players.append(aaron)


def dream_team():
    my_budget = 120
    i = 0
    splayers = sorted(players)
    my_team = []
    #Makes sure that the application doesn't allow you to pick more than 11 players
    while len(my_team) < 11:
        print("Nr.", "Name", "Price", "Pace", "Shoot")
        print("-------------------------------")

        while i < len(splayers):
            print(i, splayers[i])
            i += 1
        print("-------------------------------")
        print(Fore.CYAN + "Players needed:" + Style.RESET_ALL, 11 - len(my_team), Fore.CYAN + "Your players:" + Style.RESET_ALL, my_team,Fore.CYAN + "Remaining funds:" + Style.RESET_ALL, my_budget, "Million dollars")

        try:
            buy_player = int(input('Number you want to buy: '))
        except:
            print(Fore.RED + "Please pick a valid number" + Style.RESET_ALL)
            print("-------------------------------")
            continue

        if buy_player == 100:
            dream_team()

        if buy_player > len(splayers):
            print("Please pick a valid number")
            print("-------------------------------")
            continue

        my_budget -= splayers[int(buy_player)][1]
        if my_budget >= 0:
            my_team.append(splayers[int(buy_player)])
            print(" ")
            splayers.pop(int(buy_player))
        if my_budget < 0:
            print(Fore.RED + "No money, if you want to reset, type '100'" + Style.RESET_ALL)
            my_budget += splayers[int(buy_player)][1]
        i = 0

    print("Your final team is: ",my_team)
    print("Are you happy with this team?", Fore.GREEN + "Y" + Style.RESET_ALL, "/",Fore.RED + "N" + Style.RESET_ALL)
    confirmation = input()
    #If yes, sends data to client?
    if confirmation == 'Y':
        print("Next file yeehaw")
    #Else reset
    if confirmation == 'N':
        dream_team()

dream_team()
