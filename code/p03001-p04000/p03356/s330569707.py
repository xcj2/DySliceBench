import sys

class UFT: #Union-find tree class
    def __init__(self, N): 
        self.tree = [int(i) for i in range(N)] 
        self.rank = [0 for i in range(N)]

    def find(self, a):
        if self.tree[a] == a: return a
        else:
            self.tree[a] = self.find(self.tree[a])
            return self.tree[a]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]: self.tree[a] = b
        else:
            self.tree[b] = a
            if self.rank[a] == self.rank[b]: self.rank[a] += 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    parent = UFT(N)
    P = [int(p) - 1 for p in input().split()]
    for i in range(M):
        x, y = map(int, input().split())
        parent.unite(x-1, y-1)
    for i in range(N):
        parent.find(i)
        count = 0
    for i, p in enumerate(P):
        if parent.find(p) == parent.find(i): count += 1
    print(count)

    return 0

if __name__ == "__main__":
    solve()