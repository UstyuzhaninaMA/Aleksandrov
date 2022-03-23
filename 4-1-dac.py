import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def decimal2binary (value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while (True):
        a = input()
        if a  == 'q':
            break
        if (a.isdigit() == 0 and a[0] != '-'):
            print ("Неверный тип вводимого значения")
            continue
        a = int (a)
        if a < 0:
            print ("Введено отрицательное значение")
            continue
        if a >= 256:
            print ("Введённое значение превышает возможности восьмиразрядного ЦАП")
            continue
        list = decimal2binary (a)
        GPIO.output (dac, list)
        print ("Voltage is {:.4f}".format(3.3 * a/256))

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()