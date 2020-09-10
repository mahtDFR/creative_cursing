from gpiozero import LED
import time

led = LED(17)


def led_startup():
    led_blink = 0
    while led_blink < 5:
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)
        led_blink +=1

def tweet_sent():
    led.on()
    time.sleep(1)
    led.off()
