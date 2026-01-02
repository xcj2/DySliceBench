# UnionFind木
class UnionFind():
    def __init__(self, n):
        # その節の根、その節を含む木の高さ、その節が根の時の木のノード数
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    # 根を検索
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
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    # 木のノード数を得る
    def getSize(self, x):
        return self.size[self.find(x)]

def main():
    N,M,K = map(int, input().split())
    # 広義の友達 - 直接の友達 - ブロック
    # UnionFind木
    uftree = UnionFind(N)
    count = [0] * N
    for i in range(M):
        A,B = map(lambda x:x-1, map(int, input().split()))
        uftree.union(A,B)
        count[A] += 1
        count[B] += 1
    for i in range(K):
        C,D = map(lambda x:x-1, map(int, input().split()))
        if uftree.same_check(C,D):
            count[C] += 1
            count[D] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = uftree.getSize(i) - 1 - count[i] # 真ん中の-1は自分自身
    print(*ans)

main()
