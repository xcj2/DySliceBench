import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from bisect import bisect_right

N,K = LI()
A = LI()

P = []
Z = []
M = []
for a in A:
    if a < 0:
        M.append(a)
    elif a == 0:
        Z.append(a)
    else:
        P.append(a)

P.sort()
M.sort()

lm,lz,lp = len(M),len(Z),len(P)

nm = lm*lp
nz = lz*(lz-1)//2 + lz*(lm+lp)

if K <= nm:
    ok = 0
    ng = -10**18-1
    while abs(ok-ng) > 1:
        now = (ok+ng)//2
        num = 0
        p = -1
        for i in range(lp):
            tmp = p
            for j in range(p+1,lm):
                if P[i]*M[j] <= now:
                    tmp = j
                else:
                    break
            p = tmp
            num += p+1
        if num >= K:
            ok = now
        else:
            ng = now
    print(ok)
elif K <= nm+nz:
    print(0)
else:
    # 負数のリストを正数のリストと同様に扱えるようにする
    M = [-m for m in M]
    M.sort()
    ok = 10**18+1
    ng = 0
    while abs(ok-ng) > 1:
        now = (ok+ng)//2
        num = 0
        p = -1
        for i in range(lp)[::-1]:
            tmp = p
            for j in range(p+1,i):
                if P[i]*P[j] <= now:
                    tmp = j
                else:
                    break
            p = tmp
            num += min(p+1,i)
        p = -1
        for i in range(lm)[::-1]:
            tmp = p
            for j in range(p+1,i):
                if M[i]*M[j] <= now:
                    tmp = j
                else:
                    break
            p = tmp
            num += min(p+1,i)
        if num >= K-nm-nz:
            ok = now
        else:
            ng = now
    print(ok)