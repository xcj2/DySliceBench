import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

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

N, M, K = map(int, readline().split())
m = map(int,read().split())
fb = list(zip(m,m))

AB = fb[:M]
CD = fb[M:]
uf = UnionFind(N+1)
friends = [[] for i in range(N+1)]
for a, b in AB:
    uf.union(a, b)
    friends[a].append(b)
    friends[b].append(a)

blocks = [[] for i in range(N+1)]
for c, d in CD:
    blocks[c].append(d)
    blocks[d].append(c)

ans = []
for i in range(1, N+1):
    same_tree_size = uf.size(i)
    same_tree_block = 0
    for x in blocks[i]:
        same_tree_block += uf.same(i, x)
    n_friends = len(friends[i])
    # 「同じグループに所属する人の数」 には、iと直接友達の人、
    # iがブロックしている人i本人も含まれている
    # よって、以下でiの友達候補の人数が分かる
    # 同じグループに所属する人の数 - 同じグループ内にいるiがブロックしている人の数
    #   - 友達の数 - 1(自分)
    ans.append(str(same_tree_size - same_tree_block - n_friends - 1))

print(' '.join(ans))