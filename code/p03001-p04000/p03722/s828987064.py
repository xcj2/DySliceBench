import sys
input = sys.stdin.readline

INF = float('inf')
N, M = map(int, input().split())

class Edge():
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
    def __str__(self):
        return 'Edge: {} -> {}, cost {}'.format(self.start, self.end, self.cost)

def bellman_ford(n, es, s):
    dist = [INF] * n
    dist[s] = 0
    # 更新が止まるまで繰り返す O(V*E)
    # i度目の更新までにsを始点として0~i個の辺からなる経路が探索され、その時点の最短経路が計算される
    # 最短経路は最大でもV-1個の頂点しか通らないため、最悪でもv-1回で収束する
    cnt = 0
    while True:
        update = False
        # 辺をすべて見る
        for e in es:
            # aに到達可能かつa経由の方が近ければ更新する
            if dist[e.start] != INF and dist[e.end] > dist[e.start] + e.cost:
                dist[e.end] = dist[e.start] + e.cost
                update = True
                if cnt == n-1 and e.end == n-1:
                  print('inf')
                  sys.exit()
        cnt += 1
        # 一度も更新されなければ終了
        if not update or cnt == n:
            break
    return dist

es = []

for i in range(M):
  a, b, cost = map(int, input().split())
  es.append(Edge(a-1, b-1, -cost))
  # es.append(Edge(b-1, a-1, -cost))


print(-bellman_ford(N, es,0)[N-1])
