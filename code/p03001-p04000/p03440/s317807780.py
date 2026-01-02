from collections import defaultdict
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

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

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
            self.size[x] = 0
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            self.size[y] = 0
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # すべての頂点に対して親を検索する
    def all_find(self):
        for n in range(len(self.par)):
            self.find(n)


UF = UnionFind(N)
for i in range(M):
    x, y = map(int, input().split())
    UF.union(x, y)

UF.all_find()

# グループに分解
D = defaultdict(list)
for i in range(N):
    D[UF.par[i]].append(A[i])

# グループ数
group = len(D)
if group == 1:
    print(0)
    exit()

# 優先度付きキュー
for key in D.keys():
    heapq.heapify(D[key])

# 各グループから最低1つは選ぶ必要がある
ans = 0
for key in D.keys():
    ans += heapq.heappop(D[key])

# 残り物から小さい順に足りない分を補充（必要な辺の数: group-1, 必要な頂点数2*group-2, 不足分group-2)
remain = []
for value in D.values():
    remain.extend(value)

remain.sort()
if len(remain) < group - 2:
    print("Impossible")
else:
    ans += sum(remain[:group - 2])
    print(ans)
