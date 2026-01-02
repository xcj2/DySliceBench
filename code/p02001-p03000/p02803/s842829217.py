from copy import deepcopy
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

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

def check(ny, nx, sS):
    if 0<=ny<H and 0<=nx<W:
        if sS[ny][nx]=='.':
            return True
    else:
        return False

def bfs(sy, sx, sS):
    deq = deque()
    deq.append([(sy-1, sx-1)]) # insert indices
    sS[sy-1][sx-1] = '#'
    ddy = [-1, 0, 1, 0]
    ddx = [0, -1, 0, 1]
    step = 0
    while deq[0]:
        #print('deq', deq)
        nqueue = []
        cqueue = deq.popleft()
        for val in cqueue:
            y, x = val
            for dy, dx in zip(ddy, ddx):
                ny, nx = y+dy, x+dx
                if check(ny, nx, sS):
                    sS[ny][nx] = '#'
                    nqueue.append((ny, nx))
        deq.append(nqueue)
        if not(deq[0]):
            break
        step += 1
    return step

res = 0
for i in range(H):
    for j in range(W):
        #print('i, j:', i, j)
        if S[i][j] == '.':
            sS = deepcopy(S)
            val = bfs(i+1, j+1, sS)
            res = max(res, val)

print(res)
