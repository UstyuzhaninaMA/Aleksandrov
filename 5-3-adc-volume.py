import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)

comp = 4
troyka = 17
maxVoltage = 3.3
levels = 256


GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)
GPIO.setup (leds, GPIO.OUT, initial = GPIO.HIGH)

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
    return voltage

def leds_set (voltage):
    set = 0
    for cmp in range (8):
        if (voltage > 32*cmp):
            set = set + 2**cmp
        else:
            break
    dec_set = dec2bin (set)
    #print (dec_set)
    GPIO.output (leds, dec_set)

try:
    while True:
        lval = adc()
        lval = lval/3.3 * 256
        leds_set (lval)
        #print (lval)
        
except KeyboardInterrupt:
    print ("Программа была остановлена с клавиатуры")
else:
    print ("No exceptions")

finally:
    GPIO.output (dac, 0)
    GPIO.output (leds, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup ()