from collections import defaultdict
import sys
def input(): return sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
C = list(map(int, input().split()))
ans = [0 for i in range(Q)]
que = []
for i in range(Q):
    l, r = map(int, input().split())
    que.append((i, l, r))

Que = que.copy()

Que.sort(key=lambda x: x[-1])
point_data = defaultdict(list)

before_node = [-1 for i in range(N+1)]
for i, v in enumerate(C):
    if point_data[v]:
        before_node[i+1] = point_data[v][-1]
    point_data[v].append(i+1)

# BIT 木


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def Sum(self, i):
        s = 0
        while i:
            s += self.data[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)

    def get(self, i, j):
        return self.Sum(j)-self.Sum(i-1)


ftree = BIT(N)
for i in range(Q):
    querie, l, r = Que[i]
    if i == 0:
        for j in range(1, r+1):
            ftree.add(j, 1)
            if before_node[j] > 0:
                ftree.add(before_node[j], -1)
    else:
        for j in range(Que[i-1][-1]+1, r+1):
            ftree.add(j, 1)
            if before_node[j] > 0:
                ftree.add(before_node[j], -1)
    ans[querie] = ftree.get(l, r)
    
for i in range(Q):
    print(ans[i])