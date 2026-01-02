#ABC094-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
class WeightedUnionFind:
    def __init__(self, size):
        """
        :param collections.Iterable nodes:
        """
        self._parents = [i for i in range(size)]
        self._ranks = [0 for _ in range(size)]
        self._sizes = [1 for _ in range(size)]
        # 直近の親からの重み。root なら 0
        self._weights = [0 for _ in range(size)]
 
    def unite(self, x, y, w):
        """
        x が属する木と y が属する木を併合
        :param x:
        :param y:
        :param w: x と y の重みの差; (重み y) - (重み x)
        :return:
        """
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
 
        # rank が小さい方が下
        if self._ranks[rx] > self._ranks[ry]:
            # x が root
            self._parents[ry] = rx
            self._sizes[rx] += self._sizes[ry]
            # root 間の重みに変換
            self._weights[ry] = w + self._weights[x] - self._weights[y]
        else:
            # y が root
            self._parents[rx] = ry
            self._sizes[ry] += self._sizes[rx]
            # root 間の重みに変換
            self._weights[rx] = -w + self._weights[y] - self._weights[x]
            if self._ranks[rx] == self._ranks[ry]:
                self._ranks[ry] += 1
 
    def find(self, x):
        """
        x が属する木の root
        :param x:
        :return:
        """
        if self._parents[x] == x:
            return x
        root = self.find(self._parents[x])
        self._weights[x] += self._weights[self._parents[x]]
        self._parents[x] = root
        return root
 
    def size(self, x):
        """
        x が属する木のノード数
        :param x:
        :return:
        """
        return self._sizes[self.find(x)]
 
    def weight(self, x):
        """
        :param x:
        :return:
        """
        # 経路圧縮
        self.find(x)
        return self._weights[x]
 
    def diff(self, x, y):
        """
        (y の重み) - (x の重み)
        :param x:
        :param y:
        :return:
        """
        if self.find(x) == self.find(y):
            return self._weights[y] - self._weights[x]
        return float('inf')
n=I()
uf=WeightedUnionFind(n)
for i in range(n-1):
    u,v,w=IL()
    uf.unite(u-1,v-1,w)
C=[0]*n
for i in range(1,n):
    if uf.diff(i,0)%2==0:
        C[i]=0
    else:
        C[i]=1
for i in range(n):
    print(C[i])