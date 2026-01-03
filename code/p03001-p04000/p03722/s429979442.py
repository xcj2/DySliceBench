import sys
from heapq import *
input = sys.stdin.readline

class Bellman_Ford:
    def __init__(self, v=None, e=None, lis=None, start=None, end=None, inf=pow(10, 18)):
        self.V = v
        self.E = e
        self.lis = lis
        self.start = start if start else 0
        self.end = end if end else self.V-1
        self.inf = inf
        self.close_minus = False#負の閉路の有無
        self.count = self.V*2-1
        self.negative = [False]*self.V
        self.judge = False

    """
    リストは各要素が(始点、終点、重み)となる有向辺の集合とする(無向なら両方作る必要あり)
    Vは頂点数、Eは辺の数（これは今の所使われない）
    close_minusがTrueなら、負の閉路が存在してしまうので、注意する
    """

    def getlist(self, lis):
        self.lis = lis
    
    def def_start(self, s):
        self.start = s
    
    def def_end(self, e):
        self.end = e

    def def_inf(self, inf):
        self.inf = inf
    
    def def_vertice(self, v):
        self.V = v
    
    def def_edge(self, e):
        self.E = e
    
    def prepare(self):
        self.cost = [self.inf]*self.V # 各頂点への最小コスト
        self.cost[self.start] = 0 # 自身への距離は0

    def search(self):
        for i in range(self.V):
            update = False # 更新が行われたか
            for x, y, z in self.lis:
                if self.cost[y] > self.cost[x] + z:
                    self.cost[y] = self.cost[x] + z
                    update = True
                    if self.count <= self.V:
                        self.negative[y] = True
                    self.count -= 1
                if self.count == self.V:
                    self.judge = True
                if self.count == 0:
                    break
            if not update or not self.count:
                break
            # 負閉路が存在
            if i == self.V - 1:
                self.close_minus = True
                return False
        return True

    def main(self):#これを実行すれば良い
        self.prepare()
        self.search()
    
    def cost_all(self):
        return self.cost

def main():
    n, m = map(int,input().split())
    arrange = [None]*m

    for i in range(m):
        a, b, c = map(int, input().split())
        arrange[i] = (a-1, b-1, -c)

    bf = Bellman_Ford(v=n, e=m, lis=arrange)
    bf.main()

    for a, b, c in arrange:
        if bf.negative[a]:
            bf.negative[b] = True

    if bf.negative[n-1]:
        print("inf")
    else:
        print(-bf.cost[-1]) 


if __name__ == "__main__":
    main()