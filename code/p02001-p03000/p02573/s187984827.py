def cin():  return list(map(int,input().split()))

N, M = cin()
A = [cin() for _ in range(M)]

class UnionFind():
    
    # 要素数を指定して作成 はじめは全ての要素が別グループに属し、親はいない
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    # xの根を返す
    def find(self, x):
        if self.parents[x] < 0:  return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # xとyが属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:  return
        if self.parents[x] > self.parents[y]:  x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    # xが属するグループの要素数
    def size(self, x):  return -self.parents[self.find(x)]
    
    # ｘとyが同じグループか否か
    def same(self, x, y):  return self.find(x) == self.find(y)
    
    # xと同じメンバーの要素
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    # 根の一覧
    def roots(self):  return [i for i, x in enumerate(self.parents) if x < 0]
    
    # グループ数
    def group_count(self):  return len(self.roots())
      
uf = UnionFind(N)
for i in range(M):
    uf.union(A[i][0] - 1, A[i][1] - 1)
ans = 0
for i in range(N):
	ans = max(ans, uf.size(i))
print(ans)