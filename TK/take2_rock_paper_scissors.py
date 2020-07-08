''' try #2 
errors line 15 wins = int(results[0])
ValueError: invalid literal for int() with base 10: ''
√√√  added in the gamehistory.txt 0,0,0 as the starting stats. It can't start
with an empty stat... 
''' 

import random 

def load_results():
    text_file = open("gamehistory.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history 

def save_results( w, t, l):
    text_file = open("gamehistory.txt", "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l))
    text_file.close()

results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print(" Welcome to Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses:  %s" % (wins, ties, losses))
print("Please choose to continue the game otherwise press 9 to quit...")

computer = random.randint(1,3)
user = int(input("[1] Rock  [2] Paper  [3] Scissors  [9] Quit\n" ))

while not user == 9:
    if user == 1:
        if computer == 1:
            print("Computer chose rock... it's a tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose scissors ... computer wins :(")
            losses += 1
        else:
            print("Computer chose scissors ... you win :) ")
    elif user == 2:
        if computer == 1:
            print("Computer chose rock ... you win :) ")
            wins += 1
        elif computer == 2:
            print("Computer chose paper ... tie!")
        else: 
            print("Computer chose scissors ... computer wins!  :(")
    elif user == 3:
        if computer == 3:
            print("Computer chose rock ... computer wins! :(")
            losses += 1
        elif computer == 2:
            print("Computer chose paper ... you win! :)")
            wins += 1
        else:
            print("Computer chose scissors... it's a tie!")
            ties += 1
    else:
        print("Invaild selection. Please try again. ")
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    print("Please choose to continue ... ")
    computer = random.randint(1,3)
    user = int(input("[1] Rock  [2] Paper  [3] Scissors  [9] Quit\n"))

save_results(wins, ties, losses)