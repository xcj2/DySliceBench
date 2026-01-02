import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class UnionFind:
    def __init__(self, n):
        self.state = [-1] * n
        self.size_table = [1] * n
        # cntはグループ数
        self.cnt = n

    def root(self, u):
        v = self.state[u]
        if v < 0: return u
        self.state[u] = res = self.root(v)
        return res

    def merge(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv: return
        du = self.state[ru]
        dv = self.state[rv]
        if du > dv: ru, rv = rv, ru
        if du == dv: self.state[ru] -= 1
        self.state[rv] = ru
        self.cnt -= 1
        self.size_table[ru] += self.size_table[rv]
        return

    # グループの要素数
    def size(self, u):
        return self.size_table[self.root(u)]

def main():
    n, m, k = MI()
    uf = UnionFind(n)
    ans = [-1] * n
    for _ in range(m):
        a, b = MI1()
        uf.merge(a, b)
        ans[a]-=1
        ans[b] -= 1
    for i in range(n):ans[i]+=uf.size(i)
    for _ in range(k):
        a, b = MI1()
        if uf.root(a)==uf.root(b):
            ans[a]-=1
            ans[b]-=1
    print(*ans)

main()
