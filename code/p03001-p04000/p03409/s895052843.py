from collections import deque


class MaxFlow:
    class Edge:
        def __init__(self, to, cap, rev):
            self.to, self.cap, self.rev = to, cap, rev

    def __init__(self, node_size, inf):
        self._node = node_size
        self._inf = inf
        self._level = [-1] * self._node
        self._iter = [0] * self._node
        self._graph = [[] for _ in range(self._node)]

    def add_edge(self, from_, to, cap):
        self._graph[from_].append(self.Edge(to, cap, len(self._graph[to])))
        self._graph[to].append(self.Edge(from_, 0, len(self._graph[from_]) - 1))

    def bfs(self, start):
        self._level = [-1] * self._node
        que = deque()
        self._level[start] = 0
        que.append(start)
        while que:
            cur_vertex = que.popleft()
            for e in self._graph[cur_vertex]:
                if self._level[e.to] < 0 < e.cap:
                    self._level[e.to] = self._level[cur_vertex] + 1
                    que.append(e.to)

    def dfs(self, cur_vertex, end_vertex, flow):
        if cur_vertex == end_vertex:
            return flow
        while self._iter[cur_vertex] < len(self._graph[cur_vertex]):
            e = self._graph[cur_vertex][self._iter[cur_vertex]]
            if e.cap > 0 and self._level[cur_vertex] < self._level[e.to]:
                flowed = self.dfs(e.to, end_vertex, min(flow, e.cap))
                if flowed > 0:
                    e.cap -= flowed
                    self._graph[e.to][e.rev].cap += flowed
                    return flowed
            self._iter[cur_vertex] += 1
        return 0

    def solve(self, source, sink):
        flow = 0
        while True:
            self.bfs(source)
            if self._level[sink] < 0:
                return flow
            self._iter = [0] * self._node
            while True:
                f = self.dfs(source, sink, self._inf)
                if f == 0:
                    break
                flow += f


class BipartiteMatching:
    def __init__(self, size1, size2):
        self._u_size, self._v_size = size1, size2
        self.mf = MaxFlow(self._u_size + self._v_size + 2, min(self._u_size, self._v_size))
        for i in range(self._u_size):
            self.mf.add_edge(0, i + 1, 1)
        for i in range(self._v_size):
            self.mf.add_edge(self._u_size + i + 1, self._u_size + self._v_size + 1, 1)

    def add_edge(self, from_, to):
        self.mf.add_edge(from_ + 1, to + self._u_size + 1, 1)

    def solve(self):
        return self.mf.solve(0, self._u_size + self._v_size + 1)

#####################################################################################

N = int(input())

X = []
Y = []
for i in range(N):
    X.append([int(i) for i in input().split()])

for i in range(N):
    Y.append([int(i) for i in input().split()])

dinic = BipartiteMatching(len(X), len(Y))

for i in range(len(X)):
    for j in range(N):
        if X[i][0] < Y[j][0] and X[i][1] < Y[j][1]:
            dinic.add_edge(i,j)


print(dinic.solve())