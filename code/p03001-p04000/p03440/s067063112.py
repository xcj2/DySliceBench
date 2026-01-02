from collections import defaultdict

class UnionFind:  # 0-index
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 親の番号 要素が根の場合は-(そのグループの要素数)を格納

    def find(self, x):  # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # 要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x):  # 要素xが属するグループに属する要素をリストで返す O(n)に注意
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数を返す
        return len(self.roots())

    def all_group_members(self):  # {根: [グループに含まれる要素のリスト], ...}の辞書を返す O(n)に注意
        ret = defaultdict(list)
        for i in range(self.n):
            ret[self.find(i)].append(i)
        return ret

# ---------------------- #

n, m = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
XY = [tuple(int(x) for x in input().split()) for _ in range(m)]
B = [(a, i) for i, a in enumerate(A)]

uf = UnionFind(n)
for x, y in XY:
    uf.union(x, y)

k = n - m
if k == 1:
    print(0)
    exit()
if n < 2 * k - 2:
    print("Impossible")
    exit()

ans = 0
used = set()
for root, members in uf.all_group_members().items():
    tmp, i = min((A[x], x) for x in members)
    used.add(i)
    ans += tmp

B.sort(reverse=True)
count = 0
while count < k - 2:
    a, i = B.pop()
    if i in used:
        continue
    else:
        ans += a
        count += 1

print(ans)
