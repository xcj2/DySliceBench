#!/usr/bin/env python3
import sys
import itertools

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


h, w = MI()
Ch, Cw = MI()
Dh, Dw = MI()

S = [["#"] * (w + 4), ["#"] * (w + 4)]
for _ in range(h):
    S.append(["#", "#"] + list(ST()) + ["#", "#"])
S.append(["#"] * (w + 4))
S.append(["#"] * (w + 4))

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0))
wxy = tuple(
    (x, y)
    for x, y in itertools.product([-2, -1, 0, 1, 2], repeat=2)
    if (x, y) not in dxy
)
dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))

wq = {(Ch + 1, Cw + 1)}
cost = 0
while wq:
    q = wq
    passed = set()
    while q:
        qq = set()
        for y, x in q:
            if y == Dh + 1 and x == Dw + 1:
                print(cost)
                exit()
            passed.add((y, x))
            S[y][x] = "#"
            for dy, dx in dxy:
                ny, nx = y + dy, x + dx
                if S[ny][nx] == "#":
                    continue
                # if ny == Dh + 1 and nx == Dw + 1:
                #     print(cost)
                #     exit()
                qq.add((ny, nx))
                # S[ny][nx] = "#"
        q = qq

    # print(cost, set(passed))
    wq = set()
    for y, x in passed:
        for dy, dx in wxy:
            ny, nx = y + dy, x + dx
            if S[ny][nx] == "#":
                continue
            wq.add((ny, nx))

    cost += 1

print(-1)
