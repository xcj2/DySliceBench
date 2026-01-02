import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

def resolve():
    N, M = LI()
    AB = [LI_() for _ in range(M)]
    ans = [N*(N-1)//2]
    uf = UnionFind(N)
    for A, B in reversed(AB):
        A_size = uf.size(A)
        B_size = uf.size(B)
        connected_island_num = 0
        if not uf.same(A, B):
            connected_island_num = A_size*B_size
        ans.append(ans[-1]-connected_island_num)
        uf.unite(A, B)
    # 崩落数0の分を除去
    ans.pop()
        
    for i in reversed(ans):
        print(i)


if __name__ == '__main__':
    resolve()