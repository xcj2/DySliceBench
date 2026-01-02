from collections import Counter

n, m, k = map(int, input().split())
friends = []
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends.append((a - 1, b - 1))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

block = [[] for _ in range(n)]
for _ in range(k):
    c, d = map(int, input().split())
    block[c - 1].append(d - 1)
    block[d - 1].append(c - 1)

class Union:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0
        self.size = 1

    def get_root(self):
        n = self
        while n.parent != n:
            n = n.parent
        return n

    def find_set(self):
        return self.get_root().val


unions = []
for i in range(n):
    unions.append(Union(i))

for a, b in friends:
    x, y = unions[a], unions[b]
    if x.find_set() == y.find_set():
        continue
    x_root, y_root = x.get_root(), y.get_root()
    if x_root.rank == y_root.rank:
        y_root.parent = x_root
        x_root.rank += 1
    elif x_root.rank > y_root.rank:
        y_root.parent = x_root
    else:
        x_root.parent = y_root
    size = x_root.size + y_root.size
    x_root.size = size
    y_root.size = size

d = {}
relation = []
for i in range(n):
    u = unions[i]
    parent = u.find_set()
    relation.append(parent)

parents = Counter(relation)
for i in range(n):
    p = relation[i]
    relation[i] = [p, parents.get(p)]

ans = []
for i in range(n):
    t = relation[i][1] - 1
    parent = relation[i][0]
    for j in graph[i]:
        if relation[j][0] == parent:
            t -= 1
    for k in block[i]:
        if relation[k][0] == parent:
            t -= 1
    ans.append(t)

print(*ans)