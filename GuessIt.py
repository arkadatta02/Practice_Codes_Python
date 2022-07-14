import random
randNum = random.randint(0,100)
win = False
Turns =0
while win==False:
    guess = input("Enter a number between 1 and 100 : ")
    Turns +=1
    if randNum==int(guess):
        print("Yes... You did it! ")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if randNum>int(guess):
        print("Guess something higher. come on... ")
     else:
        print("Guess something lower. come on... ")
