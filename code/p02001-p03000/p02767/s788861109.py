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

N = I()
X = LI()

X.sort()

ans = float('inf')
for p in range(X[0],X[-1]+1):
    now = 0
    for i in range(N):
        now += (X[i]-p)**2
    if now < ans:
        ans = now

print(ans)