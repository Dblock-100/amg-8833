#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

data = 13
clock = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(data, GPIO.OUT)
GPIO.setup(clock, GPIO.IN)

for i in range(10):
    GPIO.output(data, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(data, GPIO.LOW)
    time.sleep(0.2)
    print('Switch status = ', GPIO.input(clock))

GPIO.cleanup()