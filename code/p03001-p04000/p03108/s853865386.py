class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def check(a, b):
    global uf
    global ans_list
    if uf.same(a,b):
        ans_list.append(0)
    else:
        ans_list.append(uf.size(a)*uf.size(b))
        uf.union(a,b)
    return 0




n,m = [int(_) for _ in input().split()]
l = []
for i in range(m):
    l.append([int(_) for _ in input().split()])
l.reverse()

ans_list = []
uf = UnionFind(n+1)
for i in range(m):
    a,b = l[i]
    check(a, b)
ans_list.reverse()
s = [0] * m
s[0] = ans_list[0]
for i in range(1, len(ans_list)):
    s[i] = s[i-1] + ans_list[i]
for i in range(len(s)):
    print(s[i])