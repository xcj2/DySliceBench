import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,K = II()
R,S,P = II()
T = str(input())

def calc(c):
    if c=='r':
        return P
    elif c=='s':
        return R
    else:
        return S

d = defaultdict(list)
for i in range(N):
    d[i%K].append(T[i])

ans = 0
for i in range(K):
    for j,c in enumerate(d[i]):
        if j==0:
            ans += calc(c)
            before = c
        else:
            if c!=before:
                ans += calc(c)
                before = c
            else:
                before = 'z'

print(ans)