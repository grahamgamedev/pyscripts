from gpiozero import LED, Button
from time import sleep
choice = input("Do you want full controll? ")

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

led1.on()
led2.on()
led3.on()
input("Press enter to continue. ")
led1.off()
led2.off()
led3.off()

button1 = Button(20)
button2 = Button(21)

def blink1():
    led1.blink(1,2)


def blink2():
    led2.blink(0.1,0.5)


while choice != "yes":
    button1.when_pressed = blink1
    button1.when_released = blink2
    button2.when_pressed = led1.off
    button2.when_released = led2.off
    sleep(1)
