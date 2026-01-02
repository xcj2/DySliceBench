import sys
sys.setrecursionlimit(10**7)


class SCC:
    def __init__(self,N):
        self.N = N
        self.graph = [[] for _ in range(N)]
        self.graph_rev = [[] for _ in range(N)]
        self.flag = [False]*N

    def add_edge(self,start,end):
        if start == end:
            return
        self.graph[start].append(end)
        self.graph_rev[end].append(start)

    def dfs(self,node,graph):
        self.flag[node] = True
        for n in graph[node]:
            if self.flag[n]:
                continue
            self.dfs(n,graph)
        self.order.append(node)

    def first_dfs(self):
        self.flag = [False]*self.N
        self.order = []
        for i in range(self.N):
            if self.flag[i] == False:
                self.dfs(i,self.graph)

    def second_dfs(self):
        self.flag = [False]*self.N
        self.ans = []
        for n in reversed(self.order):
            if self.flag[n]:
                continue
            self.flag[n] = True
            self.order = []
            self.dfs(n,self.graph_rev)
            self.order.reverse()
            self.ans.append(self.order)

    def scc(self):
        self.first_dfs()
        self.second_dfs()
        return self.ans


class Two_SAT():
    def __init__(self,N):
        self.N = N
        self.e = [[] for _ in range(2*N)]

    def add_condition(self,start,bool_start,end,bool_end):  # start or end という条件を考える
        self.e[start*2+(bool_start^1)].append(end*2+bool_end)
        self.e[end*2+(bool_end^1)].append(start*2+bool_start)

    def satisfiable(self):
        scc = SCC(2*self.N)
        for i in range(2*self.N):
            for j in self.e[i]:
                scc.add_edge(i,j)
        C = scc.scc()
        I = [0]*(2*self.N)
        for i in range(len(C)):
            for j in C[i]:
                I[j] = i
        res = [0]*(2*self.N)
        for i in range(self.N):
            if I[2*i] == I[2*i+1]:
                return (False,res)
            if I[2*i] < I[2*i+1]:
                res[i] = 1
        return (True,res)


def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,D = MI()
TS = Two_SAT(N)
XY = [tuple(MI()) for _ in range(N)]

for i in range(N-1):
    x1,y1 = XY[i]
    for j in range(i+1,N):
        x2,y2 = XY[j]
        if abs(x1-x2) < D:
            TS.add_condition(i,1,j,1)
        if abs(x1-y2) < D:
            TS.add_condition(i,1,j,0)
        if abs(y1-x2) < D:
            TS.add_condition(i,0,j,1)
        if abs(y1-y2) < D:
            TS.add_condition(i,0,j,0)

# 0:X,1:Y

bl,sa = TS.satisfiable()

if not bl:
    print('No')
else:
    print('Yes')
    print(*[XY[i][sa[i]] for i in range(N)],sep='\n')
