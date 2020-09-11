import random

count = 0
curses = []

list_a = open("list_a.txt", "r")
a = list_a.readlines()
list_a.close()
a = [line.rstrip() for line in a]

list_b = open("list_b.txt", "r")
b = list_b.readlines()
list_b.close()
b = [line.rstrip() for line in b]

curse = (random.choice(a) + " " + random.choice(b))
print("Generating ONE MILLION results. Please be patient, you " + curse.lower() + ".")

while count < 1000000:
    curse = (random.choice(a) + " " + random.choice(b))
    tweet = curse.upper()
    list.append(curses, tweet)
    count+=1

else:
    print("Writing results to file 'creative_curses.txt'")
    with open("creative_curses.txt", "w") as f:
        f.write("\n".join(curses))
        f.close()
    exit()