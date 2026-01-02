from collections import deque

class MaxFlow:
    class Edge:
        def __init__(self,to,cap,rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self,n,inf = 10**9+7):
        self.n = n
        self.inf = inf
        self.level = [-1]*n
        self.iter = [0]*n
        self.e = [[] for _ in range(n)]

    def add_edge(self, from_, to, cap):
        self.e[from_].append(self.Edge(to, cap, len(self.e[to])))
        self.e[to].append(self.Edge(from_, 0, len(self.e[from_])-1))

    def bfs(self, start):
        self.level = [-1]*self.n
        dq = deque()
        self.level[start] = 0
        dq.append(start)
        while dq:
            cur_vertex = dq.popleft()
            for edge in self.e[cur_vertex]:
                if edge.cap > 0 > self.level[edge.to]:
                    self.level[edge.to] = self.level[cur_vertex] + 1
                    dq.append(edge.to)

    def dfs(self, cur_vertex, end_vertex, flow):
        if cur_vertex == end_vertex:return flow
        while self.iter[cur_vertex] < len(self.e[cur_vertex]):
            edge = self.e[cur_vertex][self.iter[cur_vertex]]
            if edge.cap > 0 and self.level[cur_vertex] < self.level[edge.to]:
                flowed = self.dfs(edge.to, end_vertex, min(flow, edge.cap))
                if flowed > 0:
                    edge.cap -= flowed
                    self.e[edge.to][edge.rev].cap += flowed
                    return flowed
            self.iter[cur_vertex] += 1
        return 0

    def compute(self, source, sink):
        flow = 0
        while True:
            self.bfs(source)
            if self.level[sink] < 0:return flow
            self.iter = [0]*self.n
            while True:
                f = self.dfs(source, sink, self.inf)
                if f == 0:break
                flow += f

def main():
    x,y,e = map(int,input().split())
    mf = MaxFlow(x+y+2)
    s = x+y
    t = s+1
    for _ in range(e):
        a,b = map(int,input().split())
        mf.add_edge(a,b+x,1)
    for i in range(x):
        mf.add_edge(s,i,1)
    for i in range(y):
        mf.add_edge(i+x,t,1)
    print (mf.compute(s,t))


if __name__ == '__main__':
    main()


