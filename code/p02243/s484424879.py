from heapq import heapify, heappop, heappush, heappushpop


class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
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


def dijkstra(graph, s, N):
    '''
    graph...隣接リスト形式 リスト内要素は(ノード, エッジ長)
    s...始点ノード
    N...頂点数

    return
    ----------
    D ... 各点までの最短距離
    P ... 最短経路木における親
    '''
    pq = PriorityQueue([])
    P = [None] * N
    D = [float('inf')] * N
    D[s] = 0
    pq.push((D[s], s))  # (最短距離, 次のノード)
    while pq:
        d, v = pq.pop()
        if D[v] < d:  # この辺を扱っても最短距離にならない
            continue  # is_visitedなくてもこれを使うことで最小のものを再び探索するのを防げる
        for to, cost in graph[v]:
            if D[to] > D[v] + cost:  # v周りにおける最短経路の候補の更新
                D[to] = D[v] + cost
                pq.push((D[to], to))
                P[to] = v
    return D, P

# load datas
N = int(input())
adj = [[] for _ in range(N)]  # (node_id, 隣接要素, 隣接nodeidとコスト)の順で格納する
'''
例
[
(0について) [(1,1235), (4,65)]
(1について) [(20,6000)]
...
]
'''
for _ in range(N):
    tmp = list(map(int, input().split()))
    if tmp[1] != 0:
        node = tmp[0]
        for i in range(2, 2 + tmp[1] * 2, 2):
            adj[node].append((tmp[i], tmp[i + 1]))

D, P = dijkstra(adj, 0,N)

for i in range(N):
    print(i, D[i])
