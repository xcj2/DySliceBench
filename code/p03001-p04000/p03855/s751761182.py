from collections import defaultdict

class UnionFind():

    def __init__(self, n):
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        
        self.par[x] = y
        return


def main():
    N, K, L = map(int, input().split())
    
    uf1 = UnionFind(N)
    uf2 = UnionFind(N)

    # O(K)
    for _ in range(K):
        p, q = map(int, input().split())
        uf1.unite(p-1, q-1)
    
    # O(L)
    for _ in range(L):
        r, s = map(int, input().split())
        uf2.unite(r-1, s-1)

    # O(N) x O(log_N)
    # 理解が少し難しいが、根ペアをキーに加算していく 
    # => 根から見ると、連結している頂点数（自身を含む）を数えている。
    cnts = defaultdict(int)
    for i in range(N):
        pos = (uf1.root(i), uf2.root(i))
        cnts[pos] += 1

    ans = []
    for i in range(N):
        pos = (uf1.root(i), uf2.root(i))
        ans.append(cnts[pos])

    print(*ans)


if __name__ == '__main__':
    main()
    