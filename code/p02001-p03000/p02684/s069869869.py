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
A = LI()

visited = [-1]*N
s = 0
visited[s] = 0
count = 1
while True:
    x = A[s]-1
    if visited[x] < 0:
        visited[x] = count
        s = x
        count += 1
    else:
        break

r = count-visited[x]
y = visited[x]

if K >= y:
    k = (K-y)%r
    s = x
    for i in range(k):
        s = A[s]-1
    print(s+1)
else:
    s = 0
    for i in range(K):
        s = A[s]-1
    print(s+1)