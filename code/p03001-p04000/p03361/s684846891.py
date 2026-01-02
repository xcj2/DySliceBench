#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pri = lambda x: print(*x, sep='\n')

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

def check(ny, nx):
    if 0<=ny<H and 0<=nx<W and S[ny][nx]=='#':
        return True
    else:
        return False

ddy = [-1, 0, 1, 0]
ddx = [0, -1, 0, 1]

def dfs(y, x, S):
    deq = deque()
    deq.append([(y, x)]) # insert indices
    S[y][x] = '.'
    found = False
    while deq[0]:
        nqueue = []
        cqueue = deq.pop()
        for val in cqueue:
            y, x = val
            for dy, dx in zip(ddy, ddx):
                ny, nx = y+dy, x+dx
                if check(ny, nx):
                    found = True
                    S[ny][nx] = '.'
                    nqueue.append((ny, nx))
        if found == False:
            print('No')
            exit()
        deq.append(nqueue)

for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            dfs(y, x, S)
else:
    print('Yes')

