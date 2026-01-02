# import sys
# input = sys.stdin.readline

def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))

class UnionFind():
    def __init__(self, n):
        # uf.parentsで各ノードの親をリストで返す
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # uf.find(x)で処理を行う
        #　要素xが属するグループの根を返す（経路圧縮）
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # uf.union(x,y)で処理を行う
        # 要素xが属するグループと要素yが属するグループを併合する
        # 小さい部分木を大きい部分木にくっつける
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        # uf.size(x)で処理を行う
        # 要素xが属するグループの要素数を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):
        # uf.same(x,y)で処理を行う
        # 要素x,yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x):
        # uf.members(x)で処理を行う
        # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        # uf.roots()で処理を行う
        #　すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        # uf.group_count()で処理を行う
        # グループの数を返す
        return len(self.roots())

    def all_group_members(self):
        # all_group_members()で処理を行う
        # ｛ルート要素：[グループに属する要素のリスト]｝をdict型で返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        # ルート要素：[グループに属する要素のリスト]を文字列で返す
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n,m = mp()
uf = UnionFind(n)
used = set()
for i in range(m):
    a,b = mp()
    if (a,b) not in used:
        uf.union(a-1,b-1)
        used.add((a,b))
        used.add((b,a))
ans = -1
for i in range(n):
    ans = max(uf.size(i), ans)
print(ans)

