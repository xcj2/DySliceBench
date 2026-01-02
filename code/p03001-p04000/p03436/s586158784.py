import sys
import math
import numpy as np
from collections import Counter, defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def S():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


inf = float("inf")
mod = 10 ** 9 + 7

h, w = MI()

white = 0
s = [["#"] * (w + 2)]
for i in range(h):
    line = S()
    white += line.count(".")
    s.append(["#"] + list(line) + ["#"])
s.append(["#"] * (w + 2))
s[1][1] = "#"


dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))

step = 1
q = [(1, 1)]
while q:
    qq = []
    for x, y in q:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if s[nx][ny] == "#":
                continue
            if nx == h and ny == w:
                print(white - (step + 1))
                exit()
            qq.append((nx, ny))
            s[nx][ny] = "#"
    q = qq
    step += 1

print(-1)
