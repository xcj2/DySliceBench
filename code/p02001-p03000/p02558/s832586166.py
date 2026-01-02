class UnionFind():
    "Either 0-indexed or 1-indexed"

    __slots__ = ["parent"]

    def __init__(self, size):
        self.parent = [-1] * (size + 1)
    
    def find(self, a):
        path = []
        while self.parent[a] > 0:
            path.append(a)
            a = self.parent[a]
        for child in path:
            self.parent[child] = a
        return a

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return
        else:
            if self.parent[a] == self.parent[b]:
                self.parent[a] = b
                self.parent[b] -= 1
            elif self.parent[a] < self.parent[b]: #aのほうが大きい
                self.parent[b] = a
            else:
                self.parent[a] = b #bのほうが大きい
        
    def same(self, a, b):
        return self.find(a) == self.find(b)


def main():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    ans = []
    uf = UnionFind(N)
    for _ in range(Q):
        t, u, v = map(int, input().split())
        if t:
            ans.append('1' if uf.same(u, v) else '0')
        else:
            uf.union(u, v)

    print('\n'.join(ans))


if __name__ == "__main__":
    main()