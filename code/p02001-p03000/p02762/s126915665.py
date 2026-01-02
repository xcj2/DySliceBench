from collections import defaultdict

N, M, K = map(int, input().split())
friends = defaultdict(list)
blocked = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)
for j in range(K):
    c, d = map(int, input().split())
    blocked[c - 1].append(d - 1)
    blocked[d - 1].append(c - 1)


class UF:
    def __init__(self, node_id):
        self.node_id = node_id
        self._root = self
        self._size = 1

    @property
    def root(self):
        p = self._root
        while p is not p._root:
            p = p._root
        q = self
        while q._root is not p:
            r = q._root
            q._root = p
            q = r
        return p

    @property
    def size(self):
        return self.root._size

    def merge(self, other):
        if self.root.node_id == other.root.node_id:
            return self.root
        elif self.root.node_id < other.root.node_id:
            self.root._size += other.root._size
            other._root = self.root
            return self.root
        else:
            other.root._size += self.root._size
            self._root = other.root
            return other.root


sets = [UF(i) for i in range(N)]
visited = set()
for i in range(N):
    if i in visited:
        continue
    r = sets[i]
    stack = [(i, None)]
    while stack:
        j, parent_id = stack.pop()
        if j in visited:
            continue
        visited.add(j)
        for k in friends[j]:
            if k != parent_id:
                r = r.merge(sets[k])
                if k not in visited:
                    stack.append((k, j))

ans = []
for i in range(N):
    res = sets[i].size - len(friends[i]) - 1
    root_id = sets[i].root.node_id
    for b in blocked[i]:
        if sets[b].root.node_id == root_id:
            res -= 1
    ans.append(res)
print(*ans)
