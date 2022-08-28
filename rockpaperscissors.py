import random
import sys

computer=0
player=0
def resetscores():
    global computer
    computer=0
    global player
    player=0

def playerchoice():
    playerchoice.var = input("Choose: [Rock], [Paper] or [Scissors]: ")
    print('\n')
    if playerchoice.var.upper() == "SCISSORS":
        playerchoice.var = "Scissors"
    elif playerchoice.var.upper() == "ROCK":
        playerchoice.var = "Rock"
    elif playerchoice.var.upper() == "PAPER":
        playerchoice.var = "Paper"
    else:
        print("Please choose a valid option")
        playerchoice()

def play():
    global computer
    global player
    if player==0 and computer==0:
        print(f"""Rules:

Rock beats Scissors

Scissors beat Paper

Paper beats Rock

    Player: {player}
    Computer: {computer}
    """)

    playerchoice()

    print(f"Player chose {playerchoice.var}")

    computerchoices = ["Rock", "Paper", "Scissors"]
    computerchoice = random.choice(computerchoices)

    print(f'Computer chose {computerchoice}')
    
    if computerchoice == playerchoice.var:
        print("Tie")
        computer+=1
        player+=1
    elif computerchoice == "Rock" and playerchoice.var == "Scissors" or computerchoice == "Scissors" and playerchoice.var == "Paper" or computerchoice == "Paper" and playerchoice.var == "Rock":
        print("Computer won")
        computer+=1
    elif playerchoice.var == "Rock" and computerchoice == "Scissors" or playerchoice.var == "Scissors" and computerchoice == "Paper" or playerchoice.var == "Paper" and computerchoice == "Rock":
        print("Player won")
        player+=1
    print()
    print(f"""Player: {player}
Computer: {computer}
""")
    if computer>player:
        print(f"Computer is winning by {computer-player}")
    elif player>computer:
        print(f"Player is winning by {player-computer}")
    elif player==computer:
        print("Tie between Player and Computer")
    print('\n')
    
    playagain = 0
    while playagain != "N" or playagain != "Y" :
        playagain = input("Play Again?: [Y]/[N]/[R]eset scores: ")
        if playagain.upper() == "Y":
            play()
        elif playagain.upper() == "N":
            sys.exit()
        elif playagain.upper() == "R":
            resetscores()
            print(f"""Player: {player}
Computer: {computer}
""")
        else:
            print("Please choose a valid option")

play()