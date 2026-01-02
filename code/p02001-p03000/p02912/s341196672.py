import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

import heapq

N,M = II()
A = III()

a = [(-x,x) for x in A]
heapq.heapify(a)

for _ in range(M):
    y = heapq.heappop(a)
    heapq.heappush(a,(y[0]/2, y[1]/2))

ans = 0
for i in range(N):
    ans += math.floor(a[i][1])

print(ans)