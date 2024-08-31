#This is a small rock, paper, scissors project I'm making.
#Sekun Oshikanlu
import random
name = input("What's your name? ")

def main():
    pick = "rock", "paper", "scissors"
    cmpChoice = pick[random.randrange(0,3)]
    pChoice = input("What will you throw?(Rock, Paper, Scissors) ").lower()
    if pChoice in pick:
        if cmpChoice == pChoice:
            print("It's a tie!!!")
        elif cmpChoice == "rock":
            if pChoice == "paper":
                print("You win!!!")
            else:
                print("I win!!!")
        elif cmpChoice == "paper":
            if pChoice == "scissors":
                print("You win!!!")
            else:
                print("I win!!!")
        else:
            if pChoice == "rock":
                print("You win!!!")
            else:
                print("I win!!!")
        print(f"I threw {cmpChoice}.")
    else:
        print("That's not a real throw...")

while True:
    play = input(f"Do you want to play rock, paper, scissors {name}?(y/n) ")
    if play == "y":
        main()
    elif play == "n":
        print("Okay bro...")
        break
    else:
        continue
