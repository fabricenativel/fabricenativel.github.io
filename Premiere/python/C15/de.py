from microbit import *
from random import randint
while True:
    if accelerometer.was_gesture("shake"):
        de = randint(1,6)
        display.show(str(de))
        sleep(3000)
    display.show(Image.ASLEEP)