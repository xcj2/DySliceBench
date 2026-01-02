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

for i in range(N):
    A[i] = str(format(A[i],'b')).zfill(60)

ans = 0
for i in range(60):
    zc = 0
    oc = 0
    for j in range(N):
        if A[j][59-i]=='0':
            zc += 1
        else:
            oc += 1
    ans += 2**i*zc*oc
    ans %= mod
print(ans)