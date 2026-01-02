import sys
def input(): return sys.stdin.readline().strip()
N,M,K = map(int,input().split())
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

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

uni = UnionFind(N)
friends = []

for _ in range(M):
    a,b = l_in()
    uni.union(a-1, b-1)
    friends.append((a-1, b-1))

blocks = []

for _ in range(K):
    c,d = l_in()
    blocks.append((c-1, d-1))

res = [uni.size(i)-1 for i in range(N)]

for a,b in friends:
    res[a] -= 1
    res[b] -= 1

for c,d in blocks:
    if uni.same(c, d):
        res[c] -= 1
        res[d] -= 1

print_l(res)
