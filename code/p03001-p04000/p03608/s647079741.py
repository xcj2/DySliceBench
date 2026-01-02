from collections import Counter
from collections import deque
from functools import reduce
from pprint import pprint
import itertools
import bisect
import copy
import fractions
import math
import random
import sys
import time
import queue
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
def GCD_LIST(numbers): return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers): return reduce(LCM, numbers)
def LCM(m, n): return (m * n // fractions.gcd(m, n))
def warshall_floyd(n):
    # 隣接行列graphを使う
    for i in range(n):  # 経由する頂点
        for j in range(n):  # 開始頂点
            for k in range(n):  # 終端
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


N, M, R = MI()
r = LI()
road = [LI() for _ in range(M)]
graph = [[INF] * N for _ in range(N)]
# pprint(graph, width=30)
distance = [[INF] * N for _ in range(N)]
for a, b, c in road:
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
for i in range(N):
    graph[i][i] = 0

q = queue.PriorityQueue()

# distance = [INF] * N
# while not q.empty():
#     cost, v = q.get()
#     if distance[v] < cost:
#         continue
#     distance[v] = cost
# 
#     for next_v in range(N):
#         if graph[v][next_v] == 0:  # 繋がっていない
#             continue
#         q.put((distance[v] + graph[v][next_v], next_v))

# for begin in range(N):
for begin in r:
    begin -= 1
    q.put((0, begin))  # begin~beginのコストは0, begin番目の頂点始点
    while not q.empty():
        cost, v = q.get()
        if distance[begin][v] < cost:
            continue
        distance[begin][v] = cost

        for next_v in range(N):
            if graph[v][next_v] == 0:
                continue
            q.put((distance[begin][v] + graph[v][next_v], next_v))

mini = INF
for permutation in itertools.permutations(r):
    tmp = 0
    # print(permutation)
    for i in range(R-1):
        tmp += distance[permutation[i]-1][permutation[i+1]-1]
    mini = min(mini, tmp)

print(mini)
