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
c = [list(input()) for _ in range(H)]

cnt = 0
for row in c:
    for chara in row:
        if chara == '#':
            cnt += 1
res = H*W - cnt

def check(ny, nx):
    if 0<=ny<=H-1 and 0<=nx<=W-1 and c[ny][nx]=='.':
        return True
    else:
        return False

deq = deque()
deq.append([(0, 0)]) # insert indices
ddy = [-1, 0, 1, 0]
ddx = [0, -1, 0, 1]
step = 0
found = False
while deq[0]:
    nqueue = []
    cqueue = deq.popleft()
    for val in cqueue:
        y, x = val
        if val==(H-1, W-1):
            found = True
            break
        for dy, dx in zip(ddy, ddx):
            ny, nx = y+dy, x+dx
            if check(ny, nx):
                c[ny][nx] = '#'
                nqueue.append((ny, nx))
    if found: break
    deq.append(nqueue)
    step += 1

if not(found):
    print(-1)
    exit()
res -= (step+1)
print(res)

