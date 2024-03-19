import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 24
GPIO.setup (pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)
try:
    duty_cycle = 0
    p.start(duty_cycle)
    time.sleep(0)
    while (True):
        print ("Pleas enter duty cycle from 0 to 100\n")
        duty_cycle = int (input())
        if duty_cycle > 100 or duty_cycle < 0:
            print ("Enter correct number\n")
            continue
        print ("Voltage = ", 3.3 / 100 * duty_cycle, "\n")
        p.start(duty_cycle)
        time.sleep(15)
except ArithmeticError:
    print ("program cancle\n")
finally :
    GPIO.output(pin, 0)
    GPIO.cleanup()