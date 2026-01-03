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

N,M = LI()
a,b = LIR(M,2)

count = [0]*(N+1)
for i in range(M):
    count[a[i]] += 1
    count[b[i]] += 1

for i in range(1,N+1):
    if count[i]%2 == 1:
        print('NO')
        exit()

print('YES')