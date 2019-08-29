import datetime
from time import sleep, time, asctime
from winsound import MessageBeep
while True:
    print("0==========0=================0=======0=======0")
    print("¦ stopwach ¦ countdown timer ¦ clock ¦ alarm ¦") 
    print("¦ (1)      ¦ (2)             ¦ (3)   ¦ (4)   ¦")
    print("0==========0=================0=======0=======0")
    choice = input("Select an option ")
    print("")

    if choice == "1":
        input("press enter to start")
        before = time()
        input("press enter to stop")
        after = time()
        print(str(round(after - before,2))+" S")
        print("")
        
    if choice == "2":
        minuets = int(input("minuets"))
        seconds = int(input("seconds"))
        secc = 0

        while minuets > 0 or seconds > 0:
            print(str(minuets) + ":" + str(seconds))
            secc += 1
            seconds -= 1
            sleep(1)
            if seconds == 0 and minuets > 0:
                seconds = 59
                minuets -= 1

        print("time up")
        print("")
        MessageBeep(0)
        sleep(2)
        MessageBeep(0)
        sleep(2)
        MessageBeep(0)
        sleep(1)
        MessageBeep(0)
        sleep(1)
        MessageBeep(0)
        sleep(1)
        MessageBeep(0)
        sleep(0.5)
        MessageBeep(0)
        sleep(0.5)
        MessageBeep(0)
        sleep(0.5)
        MessageBeep(0)

    if choice == "3":
        print(asctime()[11:16])
        print(asctime()[0:10])
        print("")

    if choice == "4":
        timeo = "0"
        alarm = str(input("set alarm h:m"))
        while timeo[:5] != alarm:
            timev = datetime.datetime.time(datetime.datetime.now())
            datetime.time(15, 8, 24, 78915)
            timeo = str(timev)
            sleep(1)
            
        print("alarm")
        MessageBeep(0)
        sleep(2)
        MessageBeep(0)
        sleep(2)
        MessageBeep(0)
        sleep(1)
        MessageBeep(0)
        sleep(1)
        MessageBeep(0)
        sleep(1)
        MessageBeep(0)
        sleep(0.5)
        MessageBeep(0)
        sleep(0.5)
        MessageBeep(0)
        sleep(0.5)
        MessageBeep(0)
