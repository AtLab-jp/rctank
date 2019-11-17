import RPi.GPIO as GPIO
import time

# 初期化
GPIO.setmode(RPi.GPIO.BOARD)
GPIO.setwarnings(False)

## ===== PINのセットアップ ==========
# LED
GPIO.setup((31, 33), GPIO.OUT)


GPIO.output(31, True)
GPIO.output(33, True)