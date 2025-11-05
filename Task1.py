RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END = '\u001b[0m'

h, w = 30, 50

for y in range(h+1):
    for x in range(w):
        if y <= 10:
            print(f"{RED}  {END}", end="")
        elif 10 < y <= 20:
            print(f"{WHITE}  {END}", end="")
        else:
            print(f"{BLUE}  {END}", end="")
    print()
