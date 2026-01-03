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

N,T = LI()
A = LI()

diff = -1
num = 0
high = 0
for i in range(N)[::-1]:
    high = max(high,A[i])
    if high-A[i] > diff:
        diff = high-A[i]
        num = 1
    elif high-A[i] == diff:
        num += 1
    else:
        continue

print(num)