import RPi.GPIO as GPIO
import time 
def dec_to_bin(number):
    return [int(element) for element in  bin(number)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)

try: 
    print ("Pleas enter any number from 0 to 255\n")
    number = input ()

    if number == "q":
        print ("Program cancel\n")
        k = 1 / 0

    try: 
        number = int (number)
    except ValueError:
        print ("Enter integer number\n")
        GPIO.output(dac, 0)
        GPIO.cleanup()
        exit()

    number = int(number)

    if number < 0 or number >= 256:
        print ("Pleas enter correct number\n")
        k = 1 / 0

    voltage = 0
    bin_num = dec_to_bin(number)
    GPIO.output (dac, bin_num)

    for i in range (0, 8, 1):
        voltage *= 2
        voltage += bin_num[i]
    print ("Expected voltage", voltage/256 * 3.3, "\n")
    time.sleep(10)

except ArithmeticError:
    print ("")
finally :
    GPIO.output(dac, 0)
    GPIO.cleanup()