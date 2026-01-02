import bisect
import collections
import sys

sys.setrecursionlimit(100000000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 62


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


N = int(input())

a = lmi()

adj = collections.defaultdict(set)
uv = llmi(N - 1)
for _u, _v in uv:
    u, v = _u - 1, _v - 1
    adj[u].add(v)
    adj[v].add(u)

trees = {}


class Tree:
    def __init__(self, index, parent_index=-1):
        self.val = a[index]
        self.index = index
        self.parent = parent_index
        self.adj = []
        for v in adj[index]:
            if v == parent_index:
                continue
            self.adj.append(Tree(v, parent_index=self.index))
        self.ans = -1
        trees[index] = self

    def __repr__(self):
        return '{}: {}'.format(self.index, [t.val for t in self.adj])

    def dp(self, current, diffs):
        v = bisect.bisect_left(current, self.val)
        if v >= len(current):
            diffs.append((v, -1))
            current.append(self.val)
        else:
            diffs.append((v, current[v]))
            current[v] = self.val
        self.ans = len(current)
        for child_tree in self.adj:
            diffs = child_tree.dp(current, diffs)
            index, val = diffs.pop()
            if val == -1:
                current.pop()
            else:
                current[index] = val


root = Tree(0)
# root.dp([], [])

current = []
diffs = []
self = root

v = bisect.bisect_left(current, self.val)
stack = [(True, root)]
while stack:
    is_start, self = stack.pop()
    if is_start:
        v = bisect.bisect_left(current, self.val)
        if v >= len(current):
            diffs.append((v, -1))
            current.append(self.val)
        else:
            diffs.append((v, current[v]))
            current[v] = self.val
        self.ans = len(current)
        for child_tree in self.adj:
            stack.append((False, child_tree))
            stack.append((True, child_tree))

            # diffs = child_tree.dp(current, diffs)
    else:
        index, val = diffs.pop()
        if val == -1:
            current.pop()
        else:
            current[index] = val

for i in range(N):
    print(trees[i].ans)
