import RPi.GPIO
import time

class GPIO():
    def __init__(self):
        RPi.GPIO.setmode(RPi.GPIO.BOARD)
        RPi.GPIO.setwarnings(False)

    def set(self, pin, mode=True):
        ## -----*----- ピンをセット -----*----- ##
        # mode: 出力/入力（True/False）
        if mode:
            RPi.GPIO.setup(pin, RPi.GPIO.OUT)
        else:
            RPi.GPIO.setup(pin, RPi.GPIO.IN)

    def out(self, pin, out):
        ## -----*----- 出力 -----*----- ##
        RPi.GPIO.output(pin, out)

    def pwm(self, pin, duty, freq=1000):
        ## -----*----- PWM制御 -----*----- ##
        p = RPi.GPIO.PWM(pin, freq)
        p.start(duty)
        return p
