# Snake, Water, Gun Game
'''
Game Rules:

Three Options: Players simultaneously choose one of three options:
Snake (s) = 1
Water (w) = 0
Gun (g) = -1

Winning Conditions:
Snake beats Water: Snake drinks the water, winning the round.
Water beats Gun: The gun drowns in water, winning the round for Water.
Gun beats Snake: The gun kills the snake, winning the round.
'''
import random

computer = random.choice([1, 0, -1])
humanstr = input("Enter the input: ")
humandic = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}
human = humandic[humanstr]

print(f"You chose: {reverseDict[human]}\nComputer chose: {reverseDict[computer]}")

if(computer == human):
    print("It's Draw!")
else:
    if(computer == -1 and human == 1):
        print("You Win!")
    elif(computer == -1 and human == 0):
        print("You Lose!")
    elif(computer == 1 and human == 0):
        print("You Win!")
    elif(computer == 1 and human == -1):
        print("You Lose!")
    elif(computer == 0 and human == 1):
        print("You Lose!")
    elif(computer == 0 and human == -1):
        print("You Win!")
    else:
        print("Something went wrong!")
