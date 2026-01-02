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
A = [0] + III()

S = []
temp = 0
for i,a in enumerate(A):
    temp += a
    S.append((temp-i)%K)

d = defaultdict(int)
ans = 0
for i in range(N+1):
    ans += d[S[i]]
    d[S[i]] += 1
    if i-K+1>=0:
        d[S[i-K+1]] -= 1

print(ans)