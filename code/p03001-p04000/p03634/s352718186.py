""" ABC070D Transit Tree Path
"""
from collections import deque
from heapq import heapify, heappop, heappush, heappushpop


class PriorityQueue:
    """
    優先度付きキューの
    """
    def __init__(self, heap):
        self.heap = heap
        heapify(self.heap)
    
    def push(self, item):
        heappush(self.heap, item)
    
    def pop(self):
        return heappop(self.heap)
    
    def pushpop(self, item):
        return heappushpop(self.heap, item)
    
    def __call__(self):
        return self.heap
    
    def __len__(self):
        return len(self.heap)


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))

Q, K = map(int, input().split())
INF = float("inf")


def dijkstra(adj: list, s: int):
    Color = [0]*N # 0: 未訪問 1: Seen 2: Visited
    D = [INF]*N #始点からの距離(重み)
    P = [None]*N #親

    D[s] = 0
    P[s] = None
    PQ = PriorityQueue([(0, s)]) #(Cost, Node)を格納し、PQにする。

    while PQ: # PQに候補がある限り

        min_cost, u = PQ.pop() # 最小コストなノードu

        Color[u] = 2 # uをVisitedに。

        if D[u] < min_cost:
            # 更新の必要なし.
            continue

        for adj_idx, adj_w in adj[u]:
            if Color[adj_idx] != 2: #訪問済みでないなら
                if D[u] + adj_w < D[adj_idx]: #最小コストを更新できるなら、
                    D[adj_idx] = D[u] + adj_w
                    P[adj_idx] = u
                    # PQに(隣接要素のコスト, 隣接要素の番号)を容れる
                    PQ.push((D[adj_idx], adj_idx))
                    Color[adj_idx] = 1
    
    return D, P

D, P = dijkstra(G, s=K-1)
for q in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(D[x]+D[y])