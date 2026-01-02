from sys import stdin
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.n = n
    def find(self,x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same(self,x,y):
        return bool(self.find(x)==self.find(y))

def main():
    N,M = map(int,stdin.readline().split())
    uf = UnionFind(N)
    p = list(map(int,stdin.readline().split()))
    ans = 0
    for _ in range(M):
        x,y = map(int,stdin.readline().split())
        x -= 1
        y -= 1
        uf.union(x,y)
    for i in range(N):
        tmp = p[i]-1
        if not uf.same(tmp,i):continue
        else:ans += 1
    print(ans)
if __name__ == "__main__":
    main()