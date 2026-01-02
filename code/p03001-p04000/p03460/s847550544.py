#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    xn = []
    yn = []
    for i in range(n):
        x, y, c = input().split()
        x = int(x)
        y = int(y)
        assert c in ["W", "B"]
        if c == "W":
            y += k
        xn.append(x % (2 * k))
        yn.append(y % (2 * k))

    kibou = [[0 for x in range(2 * k + 1)] for y in range(2 * k + 1)]
    for i in range(n):
        x = xn[i]
        y = yn[i]
        squares = get_list_squares(x, y, k)
        for x1, y1, x2, y2 in squares:
            kibou[y1][x1] += 1
            kibou[y1][x2] -= 1
            kibou[y2][x1] -= 1
            kibou[y2][x2] += 1

    rui = ruiseki_2d(kibou, k)
    ma = [max(rui[y]) for y in range(2 * k)]
    print(max(ma))

def get_list_squares(x, y, k):
    # (x, y) of lower bottom
    twok = 2 * k
    assert 0 <= x < twok
    assert 0 <= y < twok
    if x >= k:
        x -= k
        y = (y + k) % (twok)
    xp = x + k
    yp = (y + k) % (twok)
    li = []
    if y < yp:
        li.append((x, y, xp, yp))
        li.append((xp, yp, twok, twok))
        if y != 0:
            li.append((xp, 0, twok, y))
        if x != 0:
            li.append((0, yp, x, twok))
        if x != 0 and  y != 0:
            li.append((0, 0, x, y))
    else:
        li.append((x, y, xp, twok))
        li.append((xp, yp, twok, y))
        if x != 0:
            li.append((0, yp, x, y))
        if y != 0:
            li.append((x, 0, xp, yp))
    return li

def ruiseki_2d(kibou, k):
    rui_1d = [[0 for x in range(2 * k)] for y in range(2 * k)]
    for y in range(k * 2):
        rui_1d[y][0] = kibou[y][0]
        for x in range(1, 2 * k):
            rui_1d[y][x] = rui_1d[y][x - 1] + kibou[y][x]

    rui_2d = [[0 for x in range(2 * k)] for y in range(2 * k)]
    for x in range(2 * k):
        rui_2d[0][x] = rui_1d[0][x]
        for y in range(1, 2 * k):
            rui_2d[y][x] = rui_2d[y - 1][x] + rui_1d[y][x]
    return rui_2d

def debug_print(arr, k):
    for y in reversed(range(2 * k)):
        print(arr[y])

main()
