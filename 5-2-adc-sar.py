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
    currsig = 0
    for value in range (8):
        currsig = currsig + 2**(7 - value)
        signal = dec2bin (currsig)
        GPIO.output (dac, signal)
        voltage = currsig / levels * maxVoltage
        time.sleep (0.01)
        compval = GPIO.input (comp)
        #print ("ADC value = {:^3} -> {}, input voltage = {:.2f}" .format (currsig, signal, voltage))
        if compval == 0:
            #print ("Это напряжение больше аналогового")
            currsig = currsig - 2**(7 - value)
        #else:
            #print ("Это напряжение меньше аналогового")
            
    print ("ADC value = {:^3} -> {}, input voltage = {:.2f}" .format (currsig, signal, voltage))

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