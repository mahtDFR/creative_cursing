from gpiozero import PWMLED

led = PWMLED(17)

def led_startup():
    led.pulse(fade_in_time=0.5,fade_out_time=0.5,n=1)

def tweet_sent():
    led.pulse(fade_in_time=0.3,fade_out_time=0.3,n=5)