import random

trun = int(input("How many times you want to play? "))
c = 0;
u = 0;

for i in range(trun):
    you = input("Type your choise from this (rock, paper, scissors): ")
    act = ["rock", "paper", "scissors"]
    comp = random.choice(act)
    print(f"\nYou have choosed {you}, computer's choice {comp}.\n")

    if you == comp:
        print(f"Oops... you both have the same choise {you}. The game is tied!...")
    elif you == "rock":
        if comp == "scissors":
            print("Congratulations!... You have won buddy...")
            u+=1
        else:
            print("he he ... better luck next time...")
            c+=1
    elif you == "paper":
        if comp == "rock":
            print("Congratulations!... You have won buddy...")
            u+=1
        else:
            print("he he ... better luck next time...")
            c+=1
    elif you == "scissors":
        if comp == "paper":
            print("Congratulations!... You have won buddy...")
            u+=1
        else:
            print("he he ... better luck next time...")
            c+=1

if(c>u):
    print("Hey looooser... Computer won the series...")
else:
    print("Thank God... You have a great luck for today...you won the series.")
