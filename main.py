import random, time

# open list_a.txt
with open ("list_a.txt") as list_a:
    a = [line.rstrip() for line in list_a]
    list_a.close()

# open list_b.txt
with open ("list_b.txt") as list_b:
    b = [line.rstrip() for line in list_b]
    list_b.close()

# main loop
while True:

    # make random combination of insults
    curse = (random.choice(a) + " " + random.choice(b))

    # generate state number for a variety of different constructions
    input = random.randint(0,5)

    # define vowels to control when to use "a" vs "an" in strings
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    if input == 0:
        print(curse.capitalize() + ".")
        #TODO preserve capitalization of list_b words if a name, e.g. "Trump" not "trump"

    # state 1
    elif input == 1:
        print(curse.capitalize() + "!")

    # state 2
    elif input == 2:
        print("You " + curse + ".")

    # state 3
    elif input == 3:
        print("You " + curse + "!")

    # state 4
    elif input == 4:
        if not curse.startswith(vowels):
            print("You're a " + curse + ".")
        else:
            print("You're an " + curse + ".")

    # state 5
    elif input == 5:
        if not curse.startswith(vowels):
            print("You're a " + curse + "!")
        else:
            print("You're an " + curse + "!")

    # delay
    time.sleep(0.5)