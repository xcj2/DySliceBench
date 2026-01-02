import sys

class UFT: #Union-find tree class
    def __init__(self, N): 
        self.tree = [int(i) for i in range(N)] 
        self.rank = [0 for i in range(N)]
        self.size = [1] * N

    def find(self, a):
        if self.tree[a] == a: return a
        else:
            self.tree[a] = self.find(self.tree[a])
            return self.tree[a]

    def findSize(self, a):
        self.tree[a] = self.find(a)
        self.size[a] = self.size[self.tree[a]]
        return self.size[a]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        asize = self.size[a]
        bsize = self.size[b]
        if a == b: return
        if self.rank[a] < self.rank[b]: 
            self.tree[a] = b
            self.size[b] += asize
        else:
            self.tree[b] = a
            self.size[a] += bsize
            if self.rank[a] == self.rank[b]: self.rank[a] += 1



def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    B = [[int(a) - 1 for a in input().split()] for _ in range(M)]
    parent = UFT(N)

    Ans = [N * (N - 1) // 2] * M
    for i in reversed(range(1, M)):
        x, y = B[i]
        if parent.find(x) != parent.find(y):
            xsize = parent.findSize(x)
            ysize = parent.findSize(y)
            parent.unite(x, y)
            Ans[i - 1] = Ans[i] - (xsize * ysize)
        else:
            Ans[i-1] = Ans[i]
    print("\n".join(map(str, Ans)))

    return 0

if __name__ == "__main__":
    solve()