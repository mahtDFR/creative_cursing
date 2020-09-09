import random, time, logging, api_keys

# logging stuff
# logging.basicConfig(filename='creative_curses.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M %p ::')

# main application starts here
# open list_a.txt
with open ("list_a.txt") as list_a:
    a = [line.rstrip() for line in list_a]
    list_a.close()

# open list_b.txt
with open ("list_b.txt") as list_b:
    b = [line.rstrip() for line in list_b]
    list_b.close()

minutes_delay = 1
delay = minutes_delay*60

# main loop
while True:

        # make random combination
        curse = (random.choice(a) + " " + random.choice(b))

        input = random.randint(1, 9)

        # e.g. "Silly bitch", "Fuck Trump"
        if input == 1:
            # string formatting...
            # TODO A horrible string capitalization method, but it works with names in the second tuple. Needs Improvement.
            curse = curse.split(" ")
            curse1 = curse[0].capitalize()
            curse2 = curse[1]
            curse = curse1 + " " + curse2

        # e.g. "Silly bitch! Fuck Trump!"
        if input == 2:
            # string formatting...
            # TODO A horrible string capitalization method, but it works with names in the second tuple. Needs Improvement.
            curse = curse.split(" ")
            curse1 = curse[0].capitalize()
            curse2 = curse[1]
            curse = curse1 + " " + curse2 + "!"

        # e.g. "Silly bitch.", "Fuck Trump."
        elif input == 3:
            # string formatting...
            # TODO A horrible string capitalization method, but it works with names in the second tuple. Needs Improvement.
            curse = curse.split(" ")
            curse1 = curse[0].capitalize()
            curse2 = curse[1]
            curse = curse1 + " " + curse2 + "."

        # e.g. "SILLY BITCH"
        elif input == 4:
            curse = curse.upper()

        # e.g. "SILLY BITCH!"
        elif input == 5:
            curse = curse.upper() + "!"

        # e.g. "SILLY BITCH."
        elif input == 6:
            curse = curse.upper() + "."

        # e.g. Same as above but it tweets it to Donald Trump
        elif input == 7:
            curse = "@realDonaldTrump " + curse.upper()

        # e.g. Same as above but it tweets it to Nigel Farage
        elif input == 8:
            curse = "@Nigel_Farage " + curse.upper()

        # e.g. Same as above but it tweets it to Boris Johnson
        elif input == 9:
            curse = "@BorisJohnson " + curse.upper()

        try:
            # post result to twitter
            print('Posting tweet "' + curse + '" to https://twitter.com/creative_curses')

            # # Tweet action (also refers to the separate api_keys file)
            api_keys.api.update_status(curse)
            # # for debugging print instead
            # print(curse)

            # logging.debug('Posted tweet "' + curse + '" to https://twitter.com/creative_curses')

            # wait for minutes_delay and begin again
            print("Sleeping for " + str(minutes_delay) + " minute(s)...")
            time.sleep(delay)

        except:
            print("Error during authentication.")
            # logging.debug("Error during authentication ' + curse + '")
            time.sleep(5)