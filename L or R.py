from random import randint
from sys import exit


while True:
    score = 0
    count = 0

    while count <= 10:
        count += 1
        rand = randint(0,1)
        if rand == 0:
            print("*")
            correct = "l"
        if rand == 1:
            print("                                                       *")
            correct = "r"
        print("left or right")
        answer = input("l or r")
        if answer == correct:
            score += 1
        print("==============================================================================")

    print(str(score) + "/10")
    if score == 10:
        print("winner")
    else:
        print("looser")

    if input("Enter play to play agan.") == "":
        exit()
    print("==============================================================================")

    
