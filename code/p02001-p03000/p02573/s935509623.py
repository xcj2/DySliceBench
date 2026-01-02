from collections import Counter
import sys
sys.setrecursionlimit(10000000)

class UnionFind:
    def __init__(self, N: int) -> None:
        #自身が親なら、その集合に属する頂点数に-1をかけたもの
        #自身が親でないなら、自身の親
        self.par = [-1 for i in range(N)]
    
    def root(self, x: int) -> bool:
        if self.par[x] < 0: #親が自分自身なら頂点
            return x
        else:
            #経路圧縮してから返す
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        else:
            if rx > ry:
                rx, ry = ry, rx
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
    
    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)
    
    def size(self, x: int) -> int:
        root = self.root(x)
        return -self.par[root]


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        uf.unite(a-1, b-1)
    
    ans = 0
    for i in range(N):
        ans = max(ans, uf.size(i))
    print(ans)

if __name__ == '__main__':
    main()