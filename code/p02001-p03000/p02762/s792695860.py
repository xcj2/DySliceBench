from collections import Counter
n, m, k = map(int, input().split())

class UnionFind:
    def __init__(self, val):
        self.parent = self
        self.val = val
        self.rank = 0
        self.size = 1

    def get_root(self):
        n = self
        while n.parent is not n:
            n = n.parent
        return n

    def find_set(self):
        return self.get_root().val


friends = []
for i in range(n + 1):
    friends.append(UnionFind(i))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    x, y = friends[a], friends[b]
    x_root, y_root = x.get_root(), y.get_root()
    if x_root.rank == y_root.rank:
        y_root.parent = x_root
        x_root.rank += 1
    elif x_root.rank > y_root.rank:
        y_root.parent = x_root
    else:
        x_root.parent = y_root

block = [[] for _ in range(n + 1)]
for _ in range(k):
    c, d = map(int, input().split())
    block[c].append(d)
    block[d].append(c)


labels = [None] * (n + 1)
parents = [0] * (n + 1)
for i in range(1, n + 1):
    u = friends[i]
    parents[i] = u.get_root().val
CounterDict = Counter(parents)

for i in range(len(parents)):
    p = parents[i]
    labels[i] = [p, CounterDict.get(p)]

ans = []
for i in range(1, n + 1):
    num = labels[i][1] - 1
    for j in graph[i]:
        if labels[i][0] == labels[j][0]:
            num -= 1
    for k in block[i]:
        if labels[i][0] == labels[k][0]:
            num -= 1
    ans.append(num)
print(*ans)