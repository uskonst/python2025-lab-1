RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

h, w = 30, 30

for y in range(h, -1, -1):
        for x in range(w + 1):
            if x*2 == y:
                print(f"{RED} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
        print()
