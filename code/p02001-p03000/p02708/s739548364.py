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

N,K = LI()

min_ = 0
for i in range(K):
    min_ += i

max_ = 0
for i in range(K):
    max_ += N-i

ans = max_-min_+1
last_max = max_
for i in range(K+1,N+2):
    min_ += i-1
    max_ += N-i+1
    ans += max_-min_+1
    ans %= mod

print(ans)