import RPi.GPIO as GPIO
import time

LED = [29, 31, 33]
MoterR = [5, 10]
MoterL = [13, 11]
POWER = 15

def setup():
    ##  -----*----- セットアップ -----*----- ##
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # LED
    GPIO.setup(LED, GPIO.OUT)
    # Moter
    GPIO.setup(MoterR, GPIO.OUT)  # RIGHT
    GPIO.setup(MoterL, GPIO.OUT) # LEFT
    GPIO.setup(POWER, GPIO.OUT)       # Vref

def led(left, right, err):
    ##  -----*----- LED制御 -----*----- ##
    # 点灯/消灯（True/False）
    GPIO.output(LED, (left, right, err))

def move(mode, power=50):
    ##  -----*----- モータ制御 -----*----- ##
    if mode == 0:
        # Forward
        GPIO.output(MoterR, (True, False))
        GPIO.output(MoterL, (True, False))
    elif mode == 1:
        # CW
        GPIO.output(MoterR, (False, True))
        GPIO.output(MoterL, (True, False))
    elif mode == 2:
        # CCW
        GPIO.output(MoterR, (True, False))
        GPIO.output(MoterL, (False, True))
    elif mode == 3:
        # Back
        GPIO.output(MoterR, (False, True))
        GPIO.output(MoterL, (False, True))
    elif mode == 4:
        # Stop
        GPIO.output(MoterR, (False, False))
        GPIO.output(MoterL, (False, False))
    power.ChangeDutyCycle(power)


setup()
# Vref(PWM)
power = GPIO.PWM(POWER, 1000)
power.start(0)  # range 0.0~100.0

led(True, False, True)

for i in range(100):
    move(i%4)
    time.sleep(0.3)