while True:
    print("0================0================0")
    print("¦ Lower to upper ¦ Upper to Lower ¦")
    print("¦ (1)            ¦ (2)            ¦")
    print("0================0================0")
    choice = input("Select an option ")
    
    if choice == "1":
        text = input("Text ")
        print(text.upper())

    if choice == "2":
        text = input("Text ")
        print(text.lower())

    print("")
