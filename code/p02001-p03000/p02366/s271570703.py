import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

class LowLink():
    def __init__(self,G):
        self.N = len(G)
        self.G = G
        self.low = [-1] * self.N
        self.ord = [-1] * self.N
    
    def _dfs(self,v,time,p = -1):
        self.ord[v] = self.low[v] = time
        time += 1

        isArticulation = False
        cnt = 0
        for e in self.G[v]:
            if self.low[e] < 0:
                cnt += 1
                self._dfs(e,time,v)
                self.low[v] = min(self.low[v],self.low[e])
                if p != -1 and self.ord[v] <= self.low[e]:
                    isArticulation = True
                if self.ord[v] < self.low[e]:
                    self.bridge.append((v,e))
            elif e != p:
                self.low[v] = min(self.low[v],self.ord[e])
        
        if p == -1 and cnt >= 2:
            isArticulation = True
        if isArticulation:
            self.articulation.append(v) 

    def build(self):
        self.articulation = []
        self.bridge = []
        self._dfs(0,0)
    

def main():
    V,E = map(int,input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    
    lowlink = LowLink(G)
    lowlink.build()
    ans = lowlink.articulation
    ans.sort()
    if ans:
        print('\n'.join(map(str,ans)))
if __name__ == '__main__':
    main()
