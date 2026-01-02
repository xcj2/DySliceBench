def getN():
    return int(input())

def getMN():
    return list(map(int, input().split()))

def getlist():
    return list(map(int, input().split()))

h, w = getlist()
hori = [[] for i in range(h)]
valt = [[] for i in range(w)]

for i in range(h):
    inp = input()
    for j, s in enumerate(inp):
        if s == "#":
            hori[i].append(j)
            valt[j].append(i)


def search(hori, w, h):
    board_h = [0 for i in range(h * w)]
    for i, retu in enumerate(hori):
        tmp = -1
        for p in retu:
            wi = p - tmp -1
            for color in range(tmp+1, p):
                board_h[color + w*i] = wi
            tmp = p

        wi = w - tmp - 1
        if retu:
            for color in range(tmp + 1, w):
                board_h[color + w * i] = wi

        else:
            for color in range(w):
                board_h[i * w + color] = w


    return board_h

def search2(hori, w, h):
    board_h = [0 for i in range(h * w)]
    for i, retu in enumerate(hori):
        tmp = -1
        for p in retu:
            wi = p - tmp -1
            for color in range(tmp+1, p):
                board_h[i + color * w] = wi
            tmp = p

        wi = h - tmp - 1
        if retu:
            for color in range(tmp + 1, h):
                board_h[i + color * w] = wi

        else:
            for color in range(h):
                board_h[i + color * w] = h
    return board_h

board_h = search(hori, w, h)
board_v = search2(valt, w, h)
# print(board_h)
# print(board_v)
# print(valt)

ans = 0
for ph, pw in zip(board_h, board_v):
    light = ph + pw - 1
    if ans < light:
        ans = light

print(ans)
"""
4 6
#..#..
......
....#.
#.#...
"""

