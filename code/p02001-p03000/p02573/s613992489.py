import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections


n,m = map(int, input().split())
par = [i for i in range(n)]
rank = [0]*n

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def main():
    for _ in range(m):
        a,b = map(int, input().split())
        unite(a-1,b-1)

    count = [0]*n
    for p in par:
        count[find(p)] += 1
    print(max(count))


if __name__ == '__main__':
    main()
