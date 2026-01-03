from collections import defaultdict

class Unionfind:

    __slots__ = ['parents','sizes']

    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n

    def root(self, x):
        if self.parents[x] == x:
            return x
        else:
            root_x = self.root(self.parents[x])
            self.parents[x] = root_x
            return root_x

    def unite(self, x, y):
        x = self.root(x); y = self.root(y)
        if x == y:
            return
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.sizes[x] += self.sizes[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    # 集合自体の数 ({1,2}, {3}, {4} : kind -> 3)
    def kind(self):
        for v in range(N):
            self.root(v)
        return len(list(set(self.parents)))

    # xが属する集合の要素の数　({1,2,3} : size(2) -> 3)
    def size(self, x):
        self.sizes[x] = self.sizes[self.root(x)]
        return self.sizes[x]

N, K, L = map(int,input().split())
road = Unionfind(N)
train = Unionfind(N)

for _ in range(K):
    p, q = map(int,input().split())
    p -= 1; q -= 1
    road.unite(p, q)

for _ in range(L):
    r, s = map(int,input().split())
    r -= 1; s -= 1
    train.unite(r, s)

cnt = defaultdict(int)

for i in range(N):
    key = (road.root(i), train.root(i))
    cnt[key] += 1

ans_list = []
for i in range(N):
    key = (road.root(i), train.root(i))
    ans = cnt[key]
    ans_list.append(ans)

print(*ans_list)