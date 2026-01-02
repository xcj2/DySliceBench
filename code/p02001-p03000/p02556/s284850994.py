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
 

N = I()
x,y = LIR(N,2)

max1 = -float('inf')
min1 = float('inf')
for i in range(N):
    max1 = max(max1,x[i]-y[i])
    min1 = min(min1,x[i]-y[i])

max2 = -float('inf')
min2 = float('inf')
for i in range(N):
    max2 = max(max2,x[i]+y[i])
    min2 = min(min2,x[i]+y[i])

print(max(max1-min1,max2-min2))