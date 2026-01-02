import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')


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

def solve():
    n, m, k = MI()
    uf = UnionFind(n)

    friends = [0] * n
    for i in range(m):
        a, b = MI1()
        uf.union(a, b)
        friends[a] += 1
        friends[b] += 1
    # print(uf.__str__())
    # print(friends)

    blocks = [0] * n
    for i in range(k):
        c, d = MI1()
        if uf.same(c, d):
            blocks[c] += 1
            blocks[d] += 1

    # print(blocks)

    ans = [0] * n

    for i in range(n):
        ans[i] = uf.size(i) - 1 - blocks[i] - friends[i]
        # print(ans)

    print(' '.join(list(map(str, ans))))

if __name__ == '__main__':
    solve()
