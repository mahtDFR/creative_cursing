import random, time, api_keys
import led_indicator

led_indicator.led_startup()
minutes_delay = 15
delay = minutes_delay * 60

while True:

    list_a = open("list_a.txt", "r")
    a = list_a.readlines()
    list_a.close()
    a = [line.rstrip() for line in a]

    list_b = open("list_b.txt", "r")
    b = list_b.readlines()
    list_b.close()
    b = [line.rstrip() for line in b]

    curse = (random.choice(a) + " " + random.choice(b))
    tweet = random.choice([curse.capitalize(), curse.upper()]) + (random.choice(["!", ".", ""]))

    # # for debugging
    # print(tweet)
    # time.sleep(1)

    api_keys.api.update_status(tweet)
    led_indicator.tweet_sent()
    time.sleep(delay)