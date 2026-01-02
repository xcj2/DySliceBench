import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x): #根を見つける、繋ぎ直す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self,x,y):
        y = self.find(y)
        x = self.find(x)
        self.parents[y] += self.parents[x]
        self.parents[x] = y
    
    def same(self,x,y):#xとyが同じグループにいるか判定
        return self.find(x) == self.find(y)


def solve(N,Q):
    parents = [-1] * N
    for i in range(1,N):
        p = int(input()) - 1
        parents[i] = p
    
    query = []
    mark = [0] * N
    mark[0] = 1
    for _ in range(Q):
        q = input().split()
        v = int(q[1]) - 1
        if q[0] == 'M':
            mark[v] += 1
            query.append((0,v))
        else:
            query.append((1,v))
    
    uf = UnionFind(N)
    for i in range(N):
        if mark[i] == 0:
            uf.unite(i,parents[i])
    
    ans = 0
    for ty,v in query[::-1]:
        if ty == 0:
            mark[v] -= 1
            if mark[v] == 0:
                uf.unite(v,parents[v])
        else:
            ans += uf.find(v) + 1
    print(ans)

def main():
    while True:
        N,M = map(int,input().split())
        if N == 0:
            return
        solve(N,M)
if __name__ == '__main__':
    main()
