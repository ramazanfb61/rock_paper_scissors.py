import random

ranNum = random.randint(1, 3)
print("\nROCK PAPER SCISSORS")
print("-Choose Number-\n1:Rock        |\n2:Paper       |\n3:Scissors    |")
print("--------------")

value = int(input("Make a decision :"))

if value == 1:
    print("You:rock")
elif value == 2:
    print("You:paper")
elif value == 3:
    print("You:scissors")

if ranNum == 1:
    print("Ai:rock")
elif ranNum == 2:
    print("Ai:paper")
elif ranNum == 3:
    print("Ai:scissors")

aiWon = "Ai Won"
draw = "draw"
youWon = "You Won"

if value == ranNum:
    print(draw)

elif value == 1 and ranNum == 2:
    print(aiWon)

elif value == 1 and ranNum == 3:
    print(youWon)

elif value == 2 and ranNum == 3:
    print(aiWon)

elif value == 2 and ranNum == 1:
    print(youWon)

elif value == 3 and ranNum == 1:
    print(aiWon)

elif value == 3 and ranNum == 2:
    print(youWon)




