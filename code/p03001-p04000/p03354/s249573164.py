class UnionFind:
    def __init__(self, n):
        self.par = [-1 for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if not x==y: # 根が同じでない場合のみ併合する
            if self.rank[x] < self.rank[y]:
                self.par[y] += self.par[x] # 要素数を併合
                self.par[x] = y # 根を付け替えている
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
        
    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y) 

def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    P = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for i in range(M)]
    A = UnionFind(N)
    
    for i in range(M):
        x,y = XY[i]
        A.union(x,y)
        
    ans = 0
    for i in range(N):
        j = i+1
        p = P[i]
        if A.same_check(j,p):
            ans += 1
    print(ans)
    
    
    
main()