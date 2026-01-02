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
    
    def unite(self,x,y): #x,yの含むグループを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x,y = y,x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self,x,y):#xとyが同じグループにいるか判定
        return self.find(x) == self.find(y)

def solve(N,M):
    edges = [tuple(map(int,input().split())) for _ in range(M)]
    edges.sort(key = lambda x:x[2])
    uf = UnionFind(N)

    ans = 0
    for a,b,c in edges:
        if uf.same(a,b):
            continue
        else:
            uf.unite(a,b)
            ans += c
    print(ans)

def main():
    while True:
        N,M = map(int,input().split())
        if N == 0:
            return
        solve(N,M)
if __name__ == '__main__':
    main()
