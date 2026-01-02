n, m, k = map(int, input().split())
a_m, b_m = [], []
c_k, d_k = [], []
def minus(x):
    return int(x)-1

friends_list = [[] for i in range(n)]
block_list = [[] for i in range(n)]
for i in range(m):
    a_m.append(0)
    b_m.append(0)
    a_m[i], b_m[i] = map(minus, input().split())
    friends_list[a_m[i]].append(b_m[i])
    friends_list[b_m[i]].append(a_m[i])
for i in range(k):
    c_k.append(0)
    d_k.append(0)
    c_k[i], d_k[i] = map(minus, input().split())
    block_list[c_k[i]].append(d_k[i])
    block_list[d_k[i]].append(c_k[i])

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents =[-1 for i in range(n)]
    # どのグループに属しているかを返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):
        return -self.parents[self.find(x)]

def blocks_in_union(x):
    count = 0
    for block in block_list[x]:
        if uf.find(x) == uf.find(block):
            count += 1
    return count

uf = UnionFind(n)
for i in range(m):
    uf.unite(a_m[i], b_m[i])
for i in range(n):
    print(uf.size(i)-1-len(friends_list[i])-blocks_in_union(i), end=' ')
