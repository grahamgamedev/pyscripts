from gpiozero import LED, Button
from time import sleep

red = LED(17)
amber = LED(27)
green = LED(22)

button1 = Button(20)
button2 = Button(21)

green.on()
amber.off()
red.off()

def stop():
    print("stop")
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()

def go():
    print("go")
    amber.on()
    red.off()
    sleep(1)
    green.on()
    amber.off()

def man():
    print("manual mode")
    state = ""
    while state != "man":
        state = input("go or stop? ")
        if state == "go":
            go()
        elif state == "stop":
            stop()

while True:
    button2.when_pressed = go
    button2.when_released = stop
    button1.when_pressed = man
    sleep(1)
