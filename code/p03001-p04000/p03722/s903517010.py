N,M = map(int,input().split())
data = [list(map(int,input().split())) for i in range(M)]

import collections

class BellmanFord():
    def __init__(self,N):
        self.N = N
        self.e = collections.defaultdict(list)
    def add(self,u,v,d,directed = False):
        if directed is False:  #無向グラフの場合
            self.e[u].append([v,d])
            self.e[v].append([u,d])
        else:  #有向グラフの場合
            self.e[u].append((v,d))
    def BellmanFord_search(self,s):  #sから各点までの最短距離
        d = collections.defaultdict(lambda: float('inf'))
        d[s] = 0
        while True:
            update = False
            for u in self.e.keys():
                for v,c in self.e[u]:
                    if d[v] > d[u] + c:
                        d[v] = d[u] + c
                        update = True
            if not update:
                break
        return d
    def BellmanFord_negative_bool(self,s):
        d = collections.defaultdict(lambda: float('inf'))
        d[s] = 0
        for i in range(self.N):
            for u in self.e.keys():
                for v,c in self.e[u]:
                    if d[v] > d[u] + c:
                        if i != self.N - 1:
                            d[v] = d[u] + c
                        else:
                            d[v] = -float('inf')
                            for i in range(self.N):
                                for u in self.e.keys():
                                    for v, c in self.e[u]:
                                        if d[v] > d[u] + c:
                                            d[v] = d[u] + c
                            if d[N] == -float('inf'):
                                return True,d
                            else:
                                return False,d
        return False,d

G = BellmanFord(N)

for i in range(M):
    G.add(data[i][0],data[i][1],-data[i][2],directed=True)

bool,d = G.BellmanFord_negative_bool(1)
if bool:
    print('inf')
    exit()

print(-d[N])