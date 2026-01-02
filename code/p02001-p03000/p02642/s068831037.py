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
A = LI()

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

b = [False]*(10**6+1)
for k in d.keys():
    if d[k]:
        b[k] = True

for i in range(10**6+1):
    if b[i]:
        for j in range(2*i,10**6+1,i):
            b[j] = False

for k in d.keys():
    if d[k] != 1:
        b[k] = False

count = 0
for i in range(10**6+1):
    if b[i]:
        count += 1

print(count) 