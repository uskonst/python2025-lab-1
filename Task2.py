WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'

h, w = 15, 30

for y in range(h+1):
    for x in range(w+1):
        if (x + y) % 15 == 0 or (x - y) % 15 == 0:
            print(f"{BLACK}  {END}", end="")
        else:
            print(f"{WHITE}  {END}", end="")
    print()
