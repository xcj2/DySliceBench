import sys
input = sys.stdin.readline

def comb(n,r):
    r = min(r,n-r)
    result = 1
    for i in range(n-r+1,n+1):
        result *= i
    for i in range(1,r+1):
        result //= i
    return result

class Unionfind:

    __slots__ = ['nodes']

    def __init__(self, n):
        self.nodes = [-1]*n

    def root(self, x):
        if self.nodes[x] < 0:
            return x
        else:
            root_x = self.root(self.nodes[x])
            self.nodes[x] = root_x
            return root_x

    def unite(self, x, y):
        x = self.root(x); y = self.root(y)
        if x == y:
            return
        rank_x = -self.nodes[x]; rank_y = -self.nodes[y]
        if rank_x < rank_y:
            x, y = y, x
        self.nodes[x] += self.nodes[y]
        self.nodes[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def rank(self, x):
        return -self.nodes[self.root(x)]

N,M = map(int,input().split())
info = [list(map(int,input().split())) for i in range(M)]
uf = Unionfind(N)
ans_list = [comb(N,2)]
ans = comb(N,2)
for A,B in info[:0:-1]:
    A -= 1; B -= 1
    if not uf.same(A,B):
        ans -= uf.rank(A) * uf.rank(B)
    uf.unite(A,B)
    ans_list.append(ans)
 
for e in ans_list[::-1]:
    print(e)