import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

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

S = list(input())
N = len(S)
d = defaultdict(int)

beki = [0]*N
now = 1
for i in range(N):
    beki[i] = now
    now *= 10
    now %= 2019

now = 0
d[0] = 1
ans = 0
for i in range(N):
    now += int(S[N-1-i])*beki[i]
    now %= 2019
    ans += d[now]
    d[now] += 1

print(ans)