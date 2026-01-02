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
    connect = dict()
    NG = [0] * N
    friend = [0] * N
    for _ in range(M):
        x, y = map(int, input().split())
        parent.unite(x-1, y-1)
        friend[x-1] += 1
        friend[y-1] += 1
    for i in range(N):
        key = parent.find(i)
        if key in connect: connect[key] += 1
        else: connect[key] = 1
    for _ in range(K):
        c, d = map(int, input().split())
        if parent.find(c-1) == parent.find(d-1):
            NG[c-1] += 1
            NG[d-1] += 1
    Ans = [0] * N
    for i in range(N):
        Ans[i] = connect[parent.find(i)] - friend[i] - NG[i] - 1
    print(" ".join(map(str, Ans)))

    return 0

if __name__ =="__main__":
    solve()