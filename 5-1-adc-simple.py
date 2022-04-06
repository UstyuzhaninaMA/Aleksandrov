import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)

comp = 4
troyka = 17
maxVoltage = 3.3
levels = 256


GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def dec2bin (value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc ():
    for value in range (256):
        signal = dec2bin (value)
        GPIO.output (dac, signal)
        voltage = value / levels * maxVoltage
        time.sleep (0.001)
        compval = GPIO.input (comp)
        if compval == 0:
            print ("ADC value = {:^3} -> {}, input voltage = {:.2f}" .format (value, signal, voltage))
            break

try:
    while True:
        adc()

except KeyboardInterrupt:
    print ("Программа была остановлена с клавиатуры")
else:
    print ("No exceptions")

finally:
    GPIO.output (dac, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup ()