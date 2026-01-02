# AC: 753 msec(Python3)
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])
  
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
           
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        return self.size[self.find(x)]


def main():
    N,M,K,*uv = map(int, read().split())
    ab, cd = uv[:2*M], uv[2*M:]

    uf = UnionFind(N)
    friend = [[] for _ in range(N+1)]
    for a, b in zip(*[iter(ab)]*2):
        uf.unite(a, b)
        friend[a].append(b)
        friend[b].append(a)
    
    ans = [uf.get_size(i) - 1 - len(friend[i]) for i in range(N+1)]

    for c, d in zip(*[iter(cd)]*2):
        if uf.is_same(c, d):
            ans[c] -= 1
            ans[d] -= 1
    
    print(*ans[1:])


if __name__ == "__main__":
    main()
