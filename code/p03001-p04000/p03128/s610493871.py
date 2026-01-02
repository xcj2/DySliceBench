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
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from functools import lru_cache

N,M = II()
A = III()
num = [0]*10
num[1],num[2],num[3],num[4],num[5] = 2,5,5,4,5
num[6],num[7],num[8],num[9] = 6,3,7,6

@lru_cache(maxsize=10**5)
def rec(n):
    val = []
    for i in range(M):
        if n-num[A[i]] < 0:
            continue
        elif n-num[A[i]] == 0:
            val.append(A[i])
        else:
            if rec(n-num[A[i]])>0:
                val.append(10*rec(n-num[A[i]])+A[i])
    if val:
        return max(val)
    else:
        return -1

print(rec(N))