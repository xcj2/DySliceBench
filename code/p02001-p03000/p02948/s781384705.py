from heapq import heappop, heappush, heappushpop, heapreplace


class HeapQueue:
    def __init__(self, reverse=False):
        self.reverse = reverse
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def append(self, p, v):
        heappush(self.heap, (-p if self.reverse else p, v))

    def appendpop(self, p, v):
        return heappushpop(self.heap, (-p if self.reverse else p, v))

    def popappend(self, p, v):
        return heapreplace(self.heap, (-p if self.reverse else p, v))

    def pop(self):
        return heappop(self.heap)[1]

    def front(self):
        return self.heap[0]


N, M = map(int, input().split())
AB = [[] for _ in range(100010)]
for _ in range(N):
    a, b = map(int, input().split())
    AB[a].append(b)
ans = 0
q = HeapQueue(reverse=True)
for i in range(M):
    for b in AB[i + 1]:
        q.append(b, b)
    if len(q):
        ans += q.pop()
print(ans)
