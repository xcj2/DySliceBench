import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read 
inp = sys.stdin.buffer.readline
def inpS(): return inp().rstrip().decode()
readlines = sys.stdin.buffer.readlines 

class UnionFind():  
    # 各要素の親要素の番号を格納するリスト
    # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 要素x, yが同じグループに属するかどうかを返す
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す (print()での表示用)
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M, K = map(int, inp().split())
uf = UnionFind(N)
ans = [0]*N
not_friend = [1]*N # 自分自身

for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  uf.union(a, b)
  not_friend[a] += 1
  not_friend[b] += 1
  
for _ in range(K):
  c, d = map(int, input().split())
  c -= 1
  d -= 1
  if uf.is_same(c, d):
    not_friend[c] += 1
    not_friend[d] += 1  
    
ans = [uf.size(i) - not_friend[i] for i in range(N)]    
print(*ans)