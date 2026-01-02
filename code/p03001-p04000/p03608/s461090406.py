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
    for i in range(n):  # 経由する頂点
        for j in range(n):  # 開始頂点
            for k in range(n):  # 終端
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


N, M, R = MI()
r = LI()
road = [LI() for _ in range(M)]
graph = [[INF] * N for _ in range(N)]
# pprint(graph, width=30)

for a, b, c in road:
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
for i in range(N):
    graph[i][i] = 0

# pprint(graph, width=30)
warshall_floyd(N)
# pprint(graph, width=30)

# for i in range(N):
#     for j in range(N):
#         if i != j and graph[i][j] != INF:
#             # i == jの場合は始点と終点が同じ
#             # INFはそもそも繋がっていない
#             print(str(i+1)+' ~ '+str(j+1)+' ===== '+str(graph[i][j]))

ans = INF 
for permutation in itertools.permutations(r):
    # print(permutation)
    tmp = 0
    for i in range(R-1):
        tmp += graph[permutation[i]-1][permutation[i+1]-1]
    ans = min(ans, tmp)
print(ans)
