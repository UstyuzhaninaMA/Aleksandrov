import RPi.GPIO as GPIO
import time

def dec2bin (value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

try:
    print ("Введите ваш период:")
    T = float(input())
    a = 0

    while True:
        while a <= 255:
            GPIO.output (dac, dec2bin (a))
            time.sleep (T/512)
            a += 1
        while a > 0:
            a -= 1
            GPIO.output (dac, dec2bin (a))
            time.sleep (T/512)

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()