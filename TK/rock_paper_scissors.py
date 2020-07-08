''' try # 1 errors, line 106, historical_data = get_historical_data()
line 34 text_file = open("history.txt", "r"). No such file or directoy. 
'''

'''
outline what you are trying to do, what the flow is
break larger task down into manageable tasks / chunks, daily breakdown 
complete one piece at a time until complete 
'''

# rock, paper, scissors 
''' 
two players - human, computer
three possible choices - rock, paper, scissors
results - win, lose, tie

# start 
- display message @ start of game 
- load persistent game stats from .txt file
- prompt user to chose: rock, paper, scissors, or quit game 
- if user picks possible choice 
    - compare with computer choice 
- if user picks random non choice
    - display message that choice was invalid
- if user picks quit
    - save new game data into .txt file 
# end 
'''


###1  display welcome message
def show_welcome_message():
    welcome_message = "Welcome to Rock, Paper, Scissors!"
    print(welcome_message)

### 2 load hisctorical_data and populate variables with data 
def get_historical_data():
    text_file = open("history.txt", "r")
    text_data = text_file.read().split(",")
    text_file.close()
    return {
        "wins": int(text_data[0]),
        "ties": int(text_data[1]),
        "losses": int(text_data[2])
    }

### 3 display historical_data_message with historical data
def show_historical_data_message():
    print(historical_data_message %
    (score["wins"], score["ties"], score["losses"]))

### 4 prompt user to make a choice between, rock ,paper, scissors, or quit
def get_user_choice():
    choice = input("[1] rock  [2] paper  [3] scissors  [9] quit\n")
    return choice_options[int(choice)]

'''
4.1 if quit, update text file with current wins, ties, losses data and 
exit game 
'''
def quit_game(wins, ties, losses):
    text_file = open("history.txt", "w")
    text_file.write(str(wins) + "," + str(ties) + "," + str(losses))
    text_file.close()

### 6? (where's 5?) compare user choice and computer choice
def compare_choices_and_get_result(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"



def display_result_message_and_update_score(result):
    if result == "tie":
        print(tie_message)
        score["ties"] += 1
    elif result == "win":
        print(win_message)
        score["wins"] += 1
    else: 
        print(loss_message)
        score["losses"] += 1 

score = {
    "wins": 0,
    "ties": 0,
    "losses": 0 
}


import random 

score = {
    "wins": 0,
    "ties": 0,
    "losses": 0 
}

welcome_message = "Welcome to Rock, Paper, Scissors!"
historical_data_message = "Wins: %s, Ties: %s, Losses: %s"
quit_message = "Thanks for playing Rock, Paper, Scissors!"
win_message = "Congrats, you won!"
loss_message = "Sorry, you lost!"
tie_message = " It was a tie."

historical_data = get_historical_data()
score["wins"] = historical_data["wins"]
score["ties"] = historical_data["ties"]
score["losses"] = historical_data["losses"]

choice_options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    9: "quit"
}

computer_choice = random.randint(1,3)

user_choice = None 