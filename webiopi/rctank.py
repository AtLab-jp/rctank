import webiopi

webiopi.setDebug()

GPIO = webiopi.GPIO


class DCMotor:
    _pin1 = 0
    _pin2 = 0

    def __init__(self, pin1, pin2):
        self._pin1 = pin1
        self._pin2 = pin2
        GPIO.setFunction(self._pin1, GPIO.PWM)
        GPIO.setFunction(self._pin2, GPIO.PWM)

    def __del__(self):
        self.write(0.0)  # stop

    def write(self, ratio):
        if 1.0 < ratio:  # saturation
            ratio = 1.0
        if -1.0 > ratio:  # saturation
            ratio = -1.0
        if 0.01 > ratio and -0.01 < ratio:  # stop
            GPIO.pwmWrite(self._pin1, 0.0)
            GPIO.pwmWrite(self._pin2, 0.0)
        elif 0 < ratio:  # Normal rotation
            GPIO.pwmWrite(self._pin1, ratio)
            GPIO.pwmWrite(self._pin2, 0.0)
        else:  # Reverse rotation
            GPIO.pwmWrite(self._pin1, 0.0)
            GPIO.pwmWrite(self._pin2, -ratio)


g_motorL = DCMotor(13, 11)  # Left motor
g_motorR = DCMotor(5, 10)  # Right motor

g_strMode = "0"  # Drive mode. GUI default mode = "0"(stop)
g_fRatio = int("5") * 0.05  # PWM Ratio. GUI default level = "5"


@webiopi.macro
def ChangeDriveMode(strMode):
    webiopi.debug("ChangeDriveMode( %s )" % (strMode))
    global g_strMode
    g_strMode = strMode
    iMode = int(strMode)
    if 0 == iMode:
        webiopi.debug("Mode : Stop")
        g_motorL.write(0.0)
        g_motorR.write(0.0)
    elif 1 == iMode:
        webiopi.debug("Mode : Forward")
        g_motorL.write(g_fRatio)
        g_motorR.write(g_fRatio)
    elif 2 == iMode:
        webiopi.debug("Mode : Backward")
        g_motorL.write(-g_fRatio)
        g_motorR.write(-g_fRatio)
    elif 3 == iMode:
        webiopi.debug("Mode : CW")
        g_motorL.write(g_fRatio)
        g_motorR.write(-g_fRatio)
    elif 4 == iMode:
        webiopi.debug("Mode : CCW")
        g_motorL.write(-g_fRatio)
        g_motorR.write(g_fRatio)


@webiopi.macro
def ChangeVoltageLevel(strLevel):
    webiopi.debug("ChangeVoltageLevel( %s )" % (strLevel))
    global g_fRatio
    g_fRatio = int(strLevel) * 0.05
    # ratio = level * 0.05 : level=10 -> ratio=0.5 -> InputVoltage=2.5[V](When VM=5[V]).
    webiopi.debug("Ratio : %f" % (g_fRatio))
    ChangeDriveMode(g_strMode)
