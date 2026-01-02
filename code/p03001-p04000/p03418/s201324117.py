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
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

N,K = II()
ans = 0
for b in range(K+1,N+1):
    i = math.floor((N-K)/b)
    ans += i*(b-K) + min(N-(K+i*b)+1, b-K)

if K==0:
    ans -= N-K

print(ans)