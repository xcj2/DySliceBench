
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

s = input()
t = input()

n = len(s)

def toi(c):
    return ord(c) - ord('a')

next_pos = array2d(n, 26, -1)

for i in range(n):
    c = toi(s[i])
    next_pos[i][c] = i

for i in range(n-2,-1,-1):
    for c in range(26):
        if next_pos[i][c] == -1 and next_pos[i+1][c] >= 0:
            next_pos[i][c] = next_pos[i+1][c]

res, now = 0, 0
for c in t:
    c = toi(c)
    if next_pos[now][c] < 0:
        res += n - now
        now = 0
        if next_pos[now][c] < 0:
            res = -1
            break
        else:
            res += next_pos[now][c] + 1
            now = next_pos[now][c] + 1
    else:
        res += next_pos[now][c] - now + 1
        now = next_pos[now][c] + 1
    now = now % n

print(res)
