import RPi.GPIO as GPIO
import time

LED = [29, 31, 33]
MoterL = [5, 10]
MoterR = [13, 11]

def setup():
    ##  -----*----- セットアップ -----*----- ##
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # LED
    GPIO.setup(LED, GPIO.OUT)
    # Moter
    GPIO.setup((5, 10), GPIO.OUT)  # RIGHT
    GPIO.setup((13, 11), GPIO.OUT) # LEFT
    GPIO.setup(15, GPIO.OUT)       # Vref

    # Vref(PWM)
    p = GPIO.PWM(15, 1000)
    p.start(50)  # range 0.0~100.0

def led(left, right, err):
    ##  -----*----- LED制御 -----*----- ##
    GPIO.output(LED, (left, right, err))


setup()
led(True, False, True)