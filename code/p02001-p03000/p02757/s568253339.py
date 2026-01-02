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

from bisect import bisect_left

N,P = LI()
S = list(map(int,list(str(input()))))

ans = 0
if P == 2:
    for i in range(N):
        if S[i]%2 == 0:
            ans += i+1
elif P == 5:
    for i in range(N):
        if S[i]%5 == 0:
            ans += i+1
else:
    M = [0]*(N+1)
    now = 0
    for i in range(N):
        now += pow(10,i,P)*S[N-1-i]
        now %= P
        M[N-1-i] = now
    d = defaultdict(list)
    for i in range(N+1):
        d[M[i]].append(i)
    for i in range(N):
        p = bisect_left(d[M[i+1]],i+1)
        ans += p

print(ans)