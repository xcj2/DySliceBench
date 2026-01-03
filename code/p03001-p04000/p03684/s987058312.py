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
    
    N = int(input())
    X = []
    Y = []
    for i in range(1,N+1):
        x,y = map(int,input().split())
        X.append([x,i])
        Y.append([y,i])
    
    X = sorted(X,key=lambda a:a[0])
    Y = sorted(Y,key=lambda a:a[0])
    DX = []
    DY = []
    for i in range(N-1):
        x1,i1 = X[i]
        x2,i2 = X[i+1]
        DX.append([abs(x1-x2),i1,i2])
        y1,i1 = Y[i]
        y2,i2 = Y[i+1]
        DY.append([abs(y1-y2),i1,i2])
    
    DX = sorted(DX,key=lambda a:a[0])
    DY = sorted(DY,key=lambda a:a[0])
    #print(DX)
    #print(DY)
        
    ans = 0
    A = UnionFind(N)
    i,j = 0,0
    c = 0
    while c < N-1:
        if i<=N-2 and j<=N-2:
            if DX[i][0] < DY[j][0]:
                cost,m1,m2 = DX[i]
                if not A.same_check(m1,m2):
                    #print(m1,m2)
                    A.union(m1,m2)
                    c += 1
                    ans += cost
                i += 1
            else:
                cost,m1,m2 = DY[j]
                if not A.same_check(m1,m2):
                    #print(m1,m2)
                    A.union(m1,m2)
                    c += 1
                    ans += cost
                j += 1
        elif i==N-1:
            cost,m1,m2 = DY[j]
            if not A.same_check(m1,m2):
                #print(m1,m2)
                A.union(m1,m2)
                c += 1
                ans += cost
            j += 1
        else:
            cost,m1,m2 = DX[i]
            if not A.same_check(m1,m2):
                #print(m1,m2)
                A.union(m1,m2)
                c += 1
                ans += cost
            i += 1
    print(ans)
        
    
    
main()