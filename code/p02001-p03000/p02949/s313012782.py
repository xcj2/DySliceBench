from collections import deque
class BellmanFord():
    def __init__(self, N):
        self.N = N
        self.edges = []
        self.to = [[] for _ in [0]*self.N]
        self.rev = [[] for _ in range(self.N)]

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
            self.to[u].append(v)
            self.rev[v].append(u)
        else:
            self.edges.append([u, v, d])
            self.to[u].append(v)
            self.rev[v].append(u)

    def BellmanFord_search(self, s):
        """
        :param s: 始点
        :return: d[i] 始点sから各点iまでの最短経路
        """
        d = [float('inf') for i in range(self.N)]
        d[s] = 0
        numEdges = len(self.edges)
        while True:
            update = False
            for i in range(numEdges):
                e = self.edges[i]
                # e: 辺iについて [from,to,cost]
                if d[e[0]] != float("inf") and d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    update = True
            if not update:
                break
        return d

    def check_reachable(self, start, to=True):
        if to:
            edges = self.to
        else:
            edges = self.rev
        visited = [0 for _ in range(self.N)]
        visited[start] = 1
        reachable = set()
        dq = deque([start])
        popleft, append = dq.popleft, dq.append

        while dq:
            current = popleft()
            reachable.add(current)
            for dest in edges[current]:
                if not visited[dest]:
                    visited[dest] = 1
                    append(dest)

        return reachable

    def BellmanFord_negative_bool(self, start, numNodes):
        # 負の閉路の検出, Trueなら負の閉路が存在する
        d = [float('inf') for _ in range(self.N)]
        d[start] = 0
        numEdges = len(self.edges)
        for i in range(numNodes):
            for j in range(numEdges):
                e = self.edges[j]
                if d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    if i == numNodes-1:
                        return True, d
        return False, d


N, M, P = map(int, input().split())
graph = BellmanFord(N)
for i in range(M):
    a, b, c = map(int, input().split())
    graph.add(a-1, b-1, -(c-P), True)

v_set = graph.check_reachable(0) & graph.check_reachable(N-1, False)
graph.edges = [edge for edge in graph.edges if edge[0] in v_set and edge[1] in v_set]
hasNegatibeCycle, dists = graph.BellmanFord_negative_bool(0, N)
if hasNegatibeCycle:
    print(-1)
else:
    print(max(0, -dists[-1]))