# The game() in a program let a user play a game and return the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains the previous Hi-Score. You need to write a program to update the Hi-Score whenever game() breaks the Hi-Score.

import random

def game():
    print("You are playing the game....")
    score = random.randint(1, 101)
    print(f"The score is: {score}")

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    if(score > hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score
game()

