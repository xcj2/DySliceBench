import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math

n, m, l = getList()

INF = 10 ** 10
vers = [[INF for j in range(n)] for i in range(n)]

for i in range(n):
    vers[i][i] = 0

for _ in range(m):
    a, b, c = getList()
    if c <= l:
        vers[a-1][b-1] = c
        vers[b - 1][a - 1] = c

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

d2 = warshall_floyd(vers)

new_vers = [[INF for j in range(n)] for i in range(n)]
for i in range(n):
    new_vers[i][i] = 0

for i in range(n):
    for j in range(n):
        if i != j and d2[i][j] <= l:
            new_vers[i][j] = 1

d3 = warshall_floyd(new_vers)

# print(d3)
Q = getN()

for _ in range(Q):
    a, b = getList()
    if d3[a-1][b-1] == INF:
        print(-1)
    else:
        print(d3[a - 1][b - 1] - 1)
