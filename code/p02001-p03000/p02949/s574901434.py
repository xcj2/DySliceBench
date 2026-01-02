import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M,P = LI()

import collections

class BellmanFord():
    def __init__(self,N):  # Nは頂点の個数
        self.N = N
        self.e = collections.defaultdict(list)
    def add(self,u,v,d,directed = False):
        if directed is False:  # 無向グラフの場合
            self.e[u].append((v,d))
            self.e[v].append((u,d))
        else:  # 有向グラフの場合
            self.e[u].append((v,d))
    def BellmanFord_negative_bool2(self,s,t):  # sから辿り着ける負の閉路で、tにたどり着けるものは存在するか
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
                            if d[t] == -float('inf'):
                                return True, d
                            else:
                                return False, d
        return False,d

G = BellmanFord(N)

for i in range(M):
    a,b,c = LI()
    G.add(a,b,P-c,directed=True)

bool,d = G.BellmanFord_negative_bool2(1,N)

if not bool:
    print(max(0,-d[N]))
else:
    print(-1)