
import collections
import itertools
import sys

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

h,w=getints()
grid=[input() for _ in range(h)]

def check(y, x):
    if grid[y][x] == '.':
        return True
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            if abs(xx - x) + abs(yy - y) != 1:
                continue
            if xx < 0 or xx >= w or yy < 0 or yy >= h:
                continue
            if grid[yy][xx] == '#':
                return True
    return False

ok = True
for i in range(h):
    for j in range(w):
        if not check(i, j):
            ok = False
            break
print("Yes" if ok else "No")