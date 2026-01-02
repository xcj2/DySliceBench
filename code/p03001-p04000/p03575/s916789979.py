from collections import deque, defaultdict
import sys
sys.setrecursionlimit(2**20)
class LowLink:
    """
    与えられたグラフの関節点と橋を求める
    Attributes:
    size: グラフの頂点数
    pre: preorderでの訪問順
    low: ### 1. prenum[u]
        ### 2. GのBackEdge(u,v)が存在する場合は、prenum[v]
        ### 3. uの全ての子childに対してlowest[child]
    articulations<list>: 関節点のリスト
    bridges<list>: 橋のリスト

    """
    def __init__(self, v):
        self.size = len(v) + 1
        self.v = v
        self.pre = [None]*self.size
        self.low = [None]*self.size
        self.articulations = []
        self.bridges = []
        for x in range(self.size):
            if self.pre[x] is None:
                self.cnt = 0
                self.dfs(x, None)
    
    def dfs(self, x, prev):
        """
        DFSにより橋と関節点を求める
        x: 現在訪れているノード
        prev: ひとつ前のノード
        """
        self.pre[x] = self.low[x] = self.cnt # 初期化
        self.cnt += 1 # 
        is_articulation = False
        n = 0 # xから出ている子の個数
        for y in self.v[x]:
            if self.pre[y] is None: #yが未訪問なら
                n += 1 # xから出ている子の個数
                low_y = self.dfs(y, x) # 再帰呼び出し
                if low_y < self.low[x]:
                    # 最小値を更新できるなら
                    self.low[x] = low_y
                if self.pre[x] <= low_y:
                    if self.pre[x]: 
                        is_articulation = True
                    if self.pre[x] < low_y:
                        self.bridges.append(
                            (min(x,y), max(x,y))
                        )
            else:
                if y != prev and self.pre[y] < self.low[x]:
                    # yが以前訪れた物ではなくて、
                    # pre[y] < low[x]なら
                    self.low[x] = self.pre[y]
        
        if prev is None and n > 1:
            # prev is None == xが根 and
            # n > 1: 根xから子が2個以上出てるなら
            is_articulation = True
        
        if is_articulation:
            self.articulations.append(x)
        
        return self.low[x]

def solve():
    V, E = map(int, input().split())
    G = defaultdict(lambda: [])
    for _ in range(E):
        s, t= map(int, input().split())
        G[s].append(t)
        G[t].append(s)
    
    #initialize
    lowlink = LowLink(G)
    #bridges
    bridges = lowlink.bridges
    print(len(bridges))

if __name__ == "__main__":
    solve()