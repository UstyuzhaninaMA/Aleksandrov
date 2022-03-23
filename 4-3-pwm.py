import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup (22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start (0)

try:
    while True:
        print ("Введите ваш коэффициент заполнения:")
        S = float(input())
        p.ChangeDutyCycle(S)
        print ("Предполагаемое напряжение равно:", 3.3 * S /100) 

finally:
    GPIO.output (22, 0)
    GPIO.cleanup()
    p.stop()