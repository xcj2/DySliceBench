class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

def renketu(Town):
    cnt = 0
    for i in range(1,len(Town.par)):
        for j in range(1,i):
            if not Town.same_check(i,j):
                return True
    return False

if __name__ == '__main__':
    N,M = list(map(int,input().split()))
    # print(Town.par)
    bridge = [list(map(int,input().split())) for i in range(M)]
    cnt = 0
    for kesu in range(M):
        Town = UnionFind(N)
        for i,(x,y) in enumerate(bridge):
            if i != kesu:
                Town.union(x,y)
        if renketu(Town):
            cnt += 1
    print(cnt)