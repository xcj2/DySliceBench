import sys
import math
from collections import deque
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        #初期化[-1]*nのリストを作る
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        #要素x,yのグループを統合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        #要素xが所属するグループの人数を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):
        #要素xとyが同じグループかどうか(同じならTrue)
        return self.find(x) == self.find(y)

    def members(self, x):
        #要素xと同じグループのメンバー全員を返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        #Find-Treeの頂点
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        #グループ数を返す
        return len(self.roots())

    def all_group_members(self):
        #頂点:[グループリスト]を返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    """
    #遷移を確認したいときはこちらに書き換えて実行する(for以降の経路圧縮が行われていない)
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)))
    """

def main():
    n, m, k = list(map(int,sys.stdin.readline().split()))
    uf = UnionFind(n)
    num_of_friends = [-1] * n

    for _ in range(m):
        a, b = list(map(int,sys.stdin.readline().split()))
        a -= 1
        b -= 1
        uf.union(a,b)
        num_of_friends[a] -= 1
        num_of_friends[b] -= 1
        #print(num_of_friends)
    #print(uf)
    """
    for i2 in range(n):
        roots[find(i2)] += 1
        print(roots)"""
    for i3 in range(n):
        num_of_friends[i3] += uf.size(i3)
        #print(num_of_friends)

    for _ in range(k):
        c, d = list(map(int,sys.stdin.readline().split()))
        c -= 1
        d -= 1
        """
        if find(c) == find(d):
            num_of_friends[c] -= 1
            num_of_friends[d] -= 1
        """
        if uf.same(c,d):
            num_of_friends[c] -= 1
            num_of_friends[d] -= 1    
    #print(num_of_friends)
    print(' '.join([str(number) for number in num_of_friends]))

if __name__ == "__main__":
    main()