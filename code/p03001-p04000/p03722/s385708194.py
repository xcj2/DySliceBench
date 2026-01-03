import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
# 一次元累積和
from itertools import accumulate
from bisect import bisect_left, bisect_right

# import numpy as np
# from scipy.special import perm
# from scipy.special import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

########
class Edge:
    def __init__(self, from_edge, to_edge, cost):
        self.from_edge = from_edge
        self.to_edge = to_edge
        self.cost = cost

def bellman_ford(start, edges, node_num):
    dist = [INF] * node_num
    dist[start] = 0
    flag = False
    for i in range(node_num):
        for edge in edges:
            if dist[edge.to_edge] > dist[edge.from_edge] + edge.cost:
                dist[edge.to_edge] = dist[edge.from_edge] + edge.cost
                if i == N-1 and edge.to_edge == (node_num - 1):
                    flag = True
    return dist, flag


N, M = l_inpl()
edges = []

for _ in range(M):
    ai, bi, ci = l_inpl()
    edges.append(Edge(ai-1, bi-1, -ci))

dist, flag = bellman_ford(0, edges, N)
# print(dist)
if flag:
    print("inf")
else:
    print(-dist[N-1])
