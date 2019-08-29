from random import randint

while True:
    print("0===============0===========0===========0")
    print("¦ Random Number ¦ Roll Dice ¦ Flip Coin ¦")
    print("¦ (1)           ¦ (2)       ¦(3)        ¦")
    print("0===============0===========0===========0")
    choice = input("Select an option ")

    if choice == "1":
        fromv = int(input("From "))
        tov = int(input("To "))
        print(randint(fromv, tov))
        print("")

    if choice == "2":
        side = randint(1, 6)
        print("")
        if side == 1:
            print("       ")
            print("   O   ")
            print("       ")

        if side == 2:
            print(" O     ")
            print("       ")
            print("     O ")

        if side == 3:
            print(" O     ")
            print("   O   ")
            print("     O ")

        if side == 4:
            print(" O   O ")
            print("       ")
            print(" O   O ")

        if side == 5:
            print(" O   O ")
            print("   O   ")
            print(" O   O ")

        if side == 6:
            print(" O   O ")
            print(" O   O ")
            print(" O   O ")

        print("")

    if choice == "3":
        side = randint(1, 2)
        print("")
        if side == 1:
            print("Heads")
        else:
            print("Tails")
        print("")
            
        

        
            
