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
S1 = list(input())
S2 = list(input())

if S1[0] == S2[0]:
    ans = 3
    start = 1
else:
    ans = 6
    start = 2

i = start
while i <= N-1:
    if S1[i] == S2[i]:
        if S1[i-1] == S2[i-1]:
            ans *= 2
            ans %= mod
        i += 1
    else:
        if S1[i-1] == S2[i-1]:
            ans *= 2
            ans %= mod
        else:
            ans *= 3
            ans %= mod
        i += 2
print(ans)