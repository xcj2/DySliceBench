class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]

        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.size[x] == self.rank[y]:
                self.rank[x] += 1

    def check_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size(self.find(x))


N, M = map(int, input().split())
lang_list = []
k_list = []
for i in range(N):
    tmp = tuple(map(int, input().split()))
    k_list.append(tmp[0])
    lang_list.append(tmp[1:])
union_find = UnionFind(M)

for lang in lang_list:
    tmp = lang[0]
    for l in lang[1:]:
        union_find.union(tmp, l)

p = union_find.find(lang_list[0][0])
for lang in lang_list[1:]:
    if p == union_find.find(lang[0]):
        continue
    else:
        print("NO")
        exit()
print("YES")

