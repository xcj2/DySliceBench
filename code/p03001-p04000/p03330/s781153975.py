#!/usr/bin/env python3
import sys
def debug(*args): print(*args, file=sys.stderr)
def exit(): sys.exit(0)

N, C = map(int, input().split())
D = []
col = []

for c in range(C):
    Drow = list(map(int, input().split()))
    D.append(Drow)
for i in range(N):
    crow = list(map(int, input().split()))
    crow = list(map(lambda x: x-1,
                    crow))
    col.append(crow)

#
count = [[0]*C for m in range(3)]

for i in range(N):
    for j in range(N):
        m = (i + j) % 3
        count[m][col[i][j]] += 1

def iwakan(y):
    res = 0
    for m in range(3):
        for c in range(C):
            res += D[c][y[m]] * count[m][c]
    return res

iwakan_list = []
for c1 in range(C):
    for c2 in range(C):
        if c1 == c2:
            continue
        for c3 in range(C):
            if (c3 == c1) or (c3 == c2):
                continue
            y = [c1, c2, c3]
            debug(y, iwakan(y))
            iwakan_list.append(iwakan(y))

print(min(iwakan_list))
