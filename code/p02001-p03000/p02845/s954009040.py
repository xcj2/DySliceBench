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

N = I()
A = III()

d = defaultdict(list)
for i in range(N):
    d[A[i]].append(i)

ans = 1
val = 3
for i in range(max(d.keys())+1):
    if len(d[i])>val:
        print(0)
        exit()
    else:
        if i==0:
            before = d[i]
            val = len(d[i])
        else:
            x = []
            for k in d[i]:
                x.append(sum([k>b for b in before]))
            z = 1
            for j,x1 in enumerate(x):
                z *= max(x1-j,0)
            if z==0:
                print(0)
                exit()
            else:
                ans *= z
                ans %= mod
            before = d[i]
m = 0
for x in d.values():
    if len(x)>=m:
        m = len(x)
if m==1:
    ans *= 3
    ans %= mod
else:
    ans *= 6
    ans %= mod

print(ans)