import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))


def dfs(i, j, c):
#    print('dfs:')
#    pri(c)
    if i<0 or j<0 or i>=len(c) or j>=len(c[0]) or c[i][j]==0:
        return
    c[i][j] = 0

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            dfs(i+di, j+dj, c)
    
    return

def solve(w, h, c):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                cnt += 1
                dfs(i, j, c)
    print(cnt)
    return


while True:
    w, h = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(h)]
    if w == h == 0:
        break
    solve(w, h, c)


