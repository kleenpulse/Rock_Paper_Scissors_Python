import random
# Rock, paper,  scissors variable
rps = ['R',
       'P',
       'S']


def py_game():
    # Player Name
    gamer = "Gamer"
    # Computer Name
    bot = 'PlasticFoods'
    # Basics
    print("""============================= \nWelcome to Rock Paper Scissors - Game:\nNote:\nGamer(You) Vs Computer(PlasticFoods)\nRock beats Scissors\nPaper beats Rock\nScissors beats Paper """)
    
    # Gets Player Input n convert to UpperCase
    player = input(
        """Enter: \n"R" for Rock\n "P" for Paper\n "S" for Scissors\n "exit" to quit the game\n""").upper()
    # Return random choice from plasticFoods
    comp_player = random.choice(rps)

    winner = 'Bye now'
    # check for valid input
    if player in rps:
        # print each player's selection
        print(f'Computer selection was: "{comp_player}"')
        print(f'Your selection was: "{player}"')

        if comp_player == player:
            winner = "Therefor Its a Tie!"

        elif comp_player == 'R' and player == 'S':
            winner = f"Rock beats Scissors,\nTherefore {bot} Wins"

        elif player == 'R' and comp_player == 'S':
            winner = f"Rock beats Scissors,\nTherefore {gamer} Wins"

        elif comp_player == 'P' and player == 'R':
            winner = f"Paper beats Rock,\nTherefore {bot} Wins"

        elif comp_player == 'R' and player == 'P':
            winner = f"Paper beats Rock,\nTherefore {gamer} Wins"
        elif comp_player == 'S' and player == 'p':
            winner = f"Scissors beats Paper,\nTherefore {bot} Wins"

        elif comp_player == 'P' and player == 'S':
            winner = f"Scissors beats Paper,\nTherefore {gamer} Wins"

    else:
        if player == 'EXIT':
            print(winner)
            quit()
        else:
            print(f'"{player}" is not a valid input\nPlease type in R or P or S only')
            restart_game()

    print(winner+'!')


def restart_game():

    py_game()


py_game()
