import random

# open list_a.txt
with open ("list_a.txt") as list_a:
    a = [line.rstrip() for line in list_a]
    list_a.close()

# open list_b.txt
with open ("list_b.txt") as list_b:
    b = [line.rstrip() for line in list_b]
    list_b.close()

creative_curses = []
count = 0

# generate ONE MILLION results and dump them in the creative_curses list
while count < 1000000:

    # make random combination
    curse = (random.choice(a) + " " + random.choice(b))

    #TODO A horrible string capitalization method, but it works with names in the second tuple. Needs Improvement.
    curse = curse.split(" ")
    curse1 = curse[0].capitalize()
    curse2 = curse[1]
    curse = curse1 + " " +  curse2

    # add result to list
    list.append(creative_curses, curse)

    # iterate
    count+=1

# When total amount is achieved, dump the list to a file
else:
    print("Writing ONE MILLION results to file 'creative_curses.txt'. Please be patient, " + curse.lower() + ".")
    with open("creative_curses.txt", "w") as f:
        f.write("\n".join(creative_curses))
        f.close()
    exit()