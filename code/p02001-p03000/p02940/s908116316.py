#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 998244353

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from bisect import bisect_left


def fact(a,M=mod):
    ans = 1
    for i in range(2,a+1):
        ans = ans*i
        ans = ans%M
    return ans

N = I()
S = str(input())

r = []
g = []
b = []

m1 = []
m2 = []
m3 = []

for i in range(3*N):
    if S[i]=='R':
        r.append(i)
    elif S[i]=='G':
        g.append(i)
    else:
        b.append(i)

for i in range(N):
    m1.append(min(r[i],g[i],b[i]))
    m2.append(sorted([r[i],g[i],b[i]])[1])
    m3.append(max(r[i],g[i],b[i]))

ans = fact(N)

for i in range(N):
    left = bisect_left(m1,m2[i])
    ans = ans*(left-i)%mod

for i in range(N)[::-1]:
    right = N-bisect_left(m3,m2[i])
    ans = ans*(right-(N-1-i))%mod

print(ans)