import RPi.GPIO as GPIO
import time 
def dec_to_bin(number):
    return [int(element) for element in  bin(number)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)

try:
    number = 0
    print ("Pleas enter any number from 0 to 8\n")
    timer = int (input())
    if timer > 8 or timer < 0:
        k = 1 / 0
    step = 1
    while (True):
        bin_num = dec_to_bin(number)
        GPIO.output (dac, bin_num)
        time.sleep(timer / 256)
        number += step
        if number == 256:
            number = 255
            step = -1
        if number == 0:
            number = 1
            step = 1
except ArithmeticError:
    print ("program cancle\n")
finally :
    GPIO.output(dac, 0)
    GPIO.cleanup()