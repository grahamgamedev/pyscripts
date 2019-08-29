from gpiozero import LED, Button
from time import sleep, time

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

button1 = Button(20)
button2 = Button(21)

print("Active")
led1.on()
led2.off()
led3.off()

def start():
    print("Started")
    led3.blink(0.5, 0.5)
    global before
    before = time()

def stop():
    print("Stoped")
    led3.off()
    after = time()
    print(str(round(after - before,2))+" S")
    print("")

while True:
    button1.when_pressed = start
    button2.when_pressed = start
    button1.when_released = stop
    button2.when_released = stop
