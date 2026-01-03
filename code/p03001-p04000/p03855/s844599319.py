class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

N,K,L = map(int,input().split())
road = UnionFind(N)
railway = UnionFind(N)
for i in range(K):
    p,q = map(int,input().split())
    road.union(p-1,q-1)
for i in range(L):
    r,s = map(int,input().split())
    railway.union(r-1,s-1)

from collections import defaultdict
d = defaultdict(lambda:0)

for i in range(N):
    p1,p2 = road.find(i),railway.find(i)
    d[(p1,p2)] += 1

ans = [str(d[(road.find(i),railway.find(i))]) for i in range(N)]
print(' '.join(ans))