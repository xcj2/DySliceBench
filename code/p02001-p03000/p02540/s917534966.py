from operator import itemgetter
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class UF_tree:
    def __init__(self, n):
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        return -self.root[self.find(x)]


N = int(input())
uf = UF_tree(N)
pos = []
for i in range(N):
    x, y = map(int, input().split())
    pos.append((x, y, i))

inf = N + 10  # 番兵

# x方向に走査
stack = [(inf, N)]
pos.sort()
for _, y, i in pos:
    while stack[-1][0] < y:
        _, j = stack.pop()
        uf.unite(j, i)
    stack.append((y, i))
stack = [(-inf, N)]
for _, y, i in pos[::-1]:
    while stack[-1][0] > y:
        _, j = stack.pop()
        uf.unite(i, j)
    stack.append((y, i))


# y方向に走査
stack = [(inf, N)]
pos.sort(key=itemgetter(1))
for x, _, i in pos:
    while stack[-1][0] < x:
        _, j = stack.pop()
        uf.unite(i, j)
    stack.append((x, i))
stack = [(-inf, N)]
for x, _, i in pos[::-1]:
    while stack[-1][0] > x:
        _, j = stack.pop()
        uf.unite(i, j)
    stack.append((x, i))

for i in range(N):
    print(uf.size(i))