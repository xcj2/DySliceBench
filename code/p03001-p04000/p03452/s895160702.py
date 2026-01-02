from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1000000)
INF = 10**10

(N, M) = reads()

edges = [[] for _ in range(N)]

for _ in range(M):
    (L, R, D) = reads()
    (L, R) = (L-1, R-1)
    edges[L].append((R, D))
    edges[R].append((L, -D))

visited = [False] * N
place = [None] * N

def walk(i):
    if visited[i]:
        return (place[i], place[i])
    visited[i] = True
    (m, M) = (INF, -INF)
    for (j, d) in edges[i]:
        if visited[j] and place[j] != place[i] + d:
            # print("v = ", visited)
            # print("p = ", place)
            print("No")
            exit()
        place[j] = place[i] + d
        (x, y) = walk(j)
        (m, M) = (min(m, x), max(M, y))
    return (m, M)

for i in range(N):
    if not visited[i]:
        place[i] = 0
        (m, M) = walk(i)
        if M - m > 10**9:
            # print("(m, M) = ", (m, M))
            print("No")
            exit()

print("Yes")


