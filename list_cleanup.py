# open lists
list_a = open("list_a.txt", "r")
a = list_a.readlines()
# list_a.close()
a = [line.rstrip() for line in a]

list_b = open("list_b.txt", "r")
b = list_b.readlines()
list_b.close()
b = [line.rstrip() for line in b]

# remove duplicates, sort alphabetically
a = (set(a))
a = sorted(a)
b = (set(b))
b = sorted(b)

# write out to same file
list_a = open("list_a.txt", "w")
list_a.write("\n".join(a))
list_a.close()

list_b = open("list_b.txt", "w")
list_b.write("\n".join(b))
list_b.close()