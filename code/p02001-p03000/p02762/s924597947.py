import sys

class UFT(): #Union-find tree class
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
    N, M, K = map(int, input().split())
    parent = UFT(N)
    NG = [0] * N
    Connected = [0] * N
    treeSize = dict()
    for _ in range(M):
        x, y = map(int, input().split())
        parent.unite(x-1, y-1)
        Connected[x-1] += 1
        Connected[y-1] += 1
    for _ in range(K):
        x, y = map(int, input().split())
        if parent.find(x-1) != parent.find(y-1): continue
        parent.unite(x-1, y-1)
        NG[x-1] += 1
        NG[y-1] += 1
    for i in range(N):
        key = parent.find(i)
        if key in treeSize: treeSize[key] += 1
        else: treeSize[key] = 1
    Ans = [0] * N
    for i in range(N):
        Ans[i] = treeSize[parent.find(i)] - Connected[i] - NG[i] - 1
    print(" ".join(map(str, Ans)))

    return 0

if __name__ =="__main__":
    solve()