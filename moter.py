from gpio import GPIO
import time

gpio = GPIO()
# LED
gpio.set(31, True)
gpio.set(33, True)
# モータ
gpio.set(5, True)
gpio.set(10, True)
gpio.set(11, True)
gpio.set(13, True)
gpio.set(15, True)
p = gpio.pwm(15, 100)

while True:
    # LED
    gpio.out(31, True)
    gpio.out(33, False)
    # モータ
    gpio.out(5, False)
    gpio.out(10, True)
    gpio.out(11, False)
    gpio.out(13, True)
    time.sleep(0.5)

    # LED
    gpio.out(31, False)
    gpio.out(33, True)
    # モータ
    gpio.out(5, True)
    gpio.out(10, False)
    gpio.out(11, True)
    gpio.out(13, True)
    time.sleep(0.5)
    print(100)
