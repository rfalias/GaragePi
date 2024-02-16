import os
import glob
import time
 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def relay_off():
    GPIO.output(8, GPIO.LOW)

def relay_on():
    GPIO.output(8, GPIO.HIGH)


def get_state():
    return GPIO.input(8)
