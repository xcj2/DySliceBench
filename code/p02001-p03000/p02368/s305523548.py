import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

class StronglyConnectedComponents:
    def __init__(self,N):
        self.N = N
        self.G = [[] for _ in range(self.N)]
        self.rG = [[] for _ in range(self.N)]
        self.group = [1] * self.N
        self.order = []
    
    def add_edge(self,u,v): # u -> v
        self.G[u].append(v)
        self.rG[v].append(u)
    
    def build(self):
        stack = []
        for s in range(self.N):
            if self.group[s] > 0:
                stack.append(s + 1)
                while stack:
                    v = stack.pop()
                    if v < 0:
                        self.order.append(- v - 1)
                    else:
                        if self.group[v - 1] > 0:
                            stack.append(-v)
                            self.group[v - 1] = -1
                            for e in self.G[v - 1]:
                                stack.append(e + 1)
        
        cnt = 0
        for s in self.order[::-1]:
            if self.group[s] < 0:
                stack.append(s)
                self.group[s] = cnt
                while stack:
                    v = stack.pop()
                    for e in self.rG[v]:
                        if self.group[e] < 0:
                            self.group[e] = cnt
                            stack.append(e)
                cnt += 1
    
    def __getitem__(self,i):
        if 0 <= i < self.N:
            return self.group[i]
        else:
            raise ValueError("StrongglyConnectedComponents index out of range")

def main():
    V,E = map(int,input().split())
    scc = StronglyConnectedComponents(V)
    for _ in range(E):
        a,b = map(int,input().split())
        scc.add_edge(a,b)
    scc.build()

    Q = int(input())
    ans = []
    for _ in range(Q):
        u,v = map(int,input().split())
        if scc[u] == scc[v]:
            ans.append('1')
        else:
            ans.append('0')
    print('\n'.join(ans))
if __name__ == '__main__':
    main()
