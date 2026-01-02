from heapq import heappop, heappush
from collections import defaultdict

class MeldableHeap():
    def __init__(self):
        self.size = 0
        self.heap = list()
        self.added = 0

    def top(self):
        if not self.heap:
            return None
        return self.heap[0] + self.added

    def pop(self):
        if not self.heap:
            return None
        res = heappop(self.heap)
        self.size -= 1
        return res + self.added

    def push(self, x):
        heappush(self.heap, x - self.added)
        self.size += 1

    def add(self, x):
        self.added += x

    def meld(self, other): #破壊的
        res = MeldableHeap()
        if self.size < other.size:
            self, other = other, self
        res.heap = self.heap
        res.size = self.size
        for _ in range(other.size):
            res.push(other.pop() - self.added)
        return res

N, M = map(int, input().split())
A = list(map(int, input().split()))
edge = [tuple(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]

for x, y in edge:
    graph[x].append(y)
    graph[y].append(x)

used = [0 for _ in range(N)]
heap = defaultdict(MeldableHeap)
roots = []

for root in range(N):
    if used[root]:
        continue
    roots.append(root)
    heap[root].push(A[root])
    used[root] = 1
    stack = [root]
    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if used[adj]:
                continue
            used[adj] = 1
            heap[root].push(A[adj])
            stack.append(adj)

single = set()

for k, v in heap.items():
    if v.size == 1:
        single.add(k)

roots.sort(key=lambda x: x in single)

res = 0
tmp = heap[roots[0]]

for i in range(1, len(roots)):
    if tmp.size == 0:
        print('Impossible')
        break
    v = heap[roots[i]]
    a = tmp.pop()
    b = v.pop()
    tmp = tmp.meld(v)
    res += a + b
else:
    print(res)