def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    C = []
    D = UnionFind(N)
    E = [0]
    ans = []
    
    for i in range(M):
        A,B = map(int, input().split())
        C.append([A,B])
    C = C[::-1]
    for i in range(M):
        A,B = C[i]
        p = D.union(A,B)
        E.append(E[i]+p)
    benri = int(N*(N-1)/2)
    for i in range(M):
        ans.append(benri - E[i])
    ans = ans[::-1]
    for i in range(M):
        print(ans[i])

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
        if not x==y:
            if self.rank[x] < self.rank[y]:
                tmp = self.par[y]
                tmp2 = self.par[x]
                self.par[y] += self.par[x]
                self.par[x] = y
                return int(self.par[y]*(self.par[y]+1)/2 - tmp*(tmp+1)/2 - tmp2*(tmp2+1)/2)
            else:
                tmp = self.par[x]
                tmp2 = self.par[y]
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
                return int(self.par[x]*(self.par[x]+1)/2 - tmp*(tmp+1)/2 - tmp2*(tmp2+1)/2)
        else:
            return 0
        

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)  

main()