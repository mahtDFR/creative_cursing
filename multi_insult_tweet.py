import random, time, api_keys

while True:

    with open("list_a.txt") as list_a:
        a = [line.rstrip() for line in list_a]
        list_a.close()

    with open("list_b.txt") as list_b:
        b = [line.rstrip() for line in list_b]
        list_b.close()

    minutes_delay = 10
    delay = minutes_delay * 60

    payload = []

    while len(payload) < 12:

        curse = (random.choice(a) + " " + random.choice(b))
        curse = curse.capitalize()
        list.append(payload, curse)

    else:
        tweet = '\n'.join(payload)
        print("Sending tweet to @creative_curses!\n")

        # print(tweet) #debug
        # time.sleep(15) #debug

        api_keys.api.update_status(tweet)
        time.sleep(delay)