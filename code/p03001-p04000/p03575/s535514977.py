class UnionFind:
    def __init__(self, num):
        self.rank = [0] * num
        self.par = [i for i in range(num)]
        self.n = num

    def find_root(self, node):
        if self.par[node] == node:
            return node
        else:
            self.par[node] = self.find_root(self.par[node])
            return self.par[node]

    def same_root(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def union(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1


def main():
    N, M = map(int, input().split())
    L = [list(map(int,input().split())) for i in range(M)]
    for i in range(M) :
        L[i][0] -= 1
        L[i][1] -= 1
    
    ans = 0
    
    for i in range(M) :
        UF = UnionFind(N)
        for j in range(M) :
            if j == i :
                continue
            UF.union(L[j][0], L[j][1])
        
        ans += (UF.same_root(L[i][0], L[i][1]) == False)
    
    print(ans)

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    main()
