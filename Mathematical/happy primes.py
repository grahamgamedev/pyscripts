n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

while True:
    print("+-*/=Happy Primes=/*-+")
    print("For help press enter.")
    number = input("Prime ")

    if number == "":
        print("Enter a number to see if it is prime or enter a prime to see if it is a happy prime. If it is not a happy prime it wont do anything.")
        print("")

    else:
        divide = 1
        prime = 1
        while prime == 1 and divide < 12:
            divide += 1
            if divide == int(number):
                divide += 1
            if int(number) % divide == 0 or number == "1":
                prime = 0
                print("Not Prime")
            
        if prime == 1:
            print("Prime")
            while int(number) > 1:
                n1 = int(number[0])
                if len(number) >= 10:
                    n2 = int(number[1])
                if len(number) >= 100:
                    n3 = int(number[2])
                if len(number) >= 1000:
                    n4 = int(number[3])
                if len(number) >= 10000:
                    n5 = int(number[4])
                if len(number) >= 100000:
                     n6 = int(number[5])

                number = str(n1 * n1 + n2 * n2 + n3 * n3 + n4 * n4 + n5 * n5 + n6 * n6)
                
            if int(number[0]) == 1:
                print("Happy Prime")
        print("")

