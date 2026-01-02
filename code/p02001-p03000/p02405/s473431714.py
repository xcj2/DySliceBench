def oddline(l: int):
    "print # and . taking turns for l-length"
    print("".join(["." if n % 2 == 0 else "#" for n in range(l)]))


def evenline(l: int):
    "print . and # taking turns for l-length"
    print("".join(["#" if n % 2 == 0 else "." for n in range(l)]))


def buildboard(s: int):
    "print a checked board with given size"
    for r in range(s[0]):
        if r % 2 == 0:
            evenline(d[1])
        else:
            oddline(d[1])
    print()  # for a blank line


while 1:
    d = tuple(map(int, input().split()))
    if d[0] == d[1] == 0:
        break
    buildboard(d)


