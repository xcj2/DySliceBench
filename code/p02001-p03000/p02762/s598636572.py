import sys
import collections

class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * (size + 1)  # 非負なら親ノード，負ならグループの要素数

    def root(self, x):  # root(x): xの根ノードを返す．
        if self.parent[x] < 0:
            return x
        elif self.parent[self.parent[x]] < 0:
            return self.parent[x]
        else:
            self.parent[x] = self.root(self.parent[x])  # xをxの根に直接つなぐ
            return self.parent[x]

    def merge(self, x, y):  # merge(x,y): xのいるグループと$y$のいるグループをまとめる
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:  # xの要素数がyの要素数より「小さい」とき入れ替える
            x, y = y, x
        self.parent[x] += self.parent[y]  # xの要素数を更新
        self.parent[y] = x  # yをxにつなぐ
        return True

    def issame(self, x, y):  # same(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)

    def size(self, x):  # size(x): xのいるグループの要素数を返す
        return -self.parent[self.root(x)]


def do():
    sys.setrecursionlimit(100000000)

    N, M, K = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(M)]
    blocks = [list(map(int, input().split())) for _ in range(K)]

    uf1 = UnionFind(N + 1) # 友達候補のUF
    friends_list= [set() for _ in range(N + 1)]
    block_list = [set() for _ in range(N + 1)]

    for query in friends :
        a,b= query
        uf1.merge(a,b)
        friends_list[a].add(b)
        friends_list[b].add(a)

    for query in blocks:
        a, b = query
        block_list[a].add(b)
        block_list[b].add(a)
    anss = []
    for i in range(1,N+1):
        s = uf1.size(i) -1 #ベースの人数

        friends = friends_list[i]
        for friend in friends:
            if uf1.issame(friend,i):
                s -=1

        blocks = block_list[i]
        for block in blocks:
            if uf1.issame(block,i):
                s -=1
        anss.append(s)
    print(*(anss))

if __name__ == "__main__":
    do()
