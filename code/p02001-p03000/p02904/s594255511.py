class BIT:
    def __init__(self, n):
        self.N = n
        self.n = 1<<n.bit_length()
        self.data = [0] * (self.n + 1)
        self.num = 0
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i
        self.num+=1
    def search(self, value):
        if value<1:
            return 0
        if value >self.num:
            return self.N+1
        x,sx = 0,0
        step = self.n
        while step:
            y = x+step
            sy = sx+self.data[y]
            if sy < value:
                x,sx = y,sy
            step >>= 1
        return x+1
class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]


    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])


    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)
from collections import deque
N, K = map(int, input().split())
P = list(map(int, input().split()))
B = BIT(N)
U = UnionFind(N)
ans = N-K+1
for i in range(K):
    B.add(P[i]+1, 1)
for i in range(1, N-K+1):
    m = B.search(1)
    M = B.search(K)
    if P[i-1]+1==m and P[i+K-1]+1>M:
        U.unite(i-1, i)
    B.add(P[i-1]+1, -1)
    B.add(P[i+K-1]+1, 1)
s, l = 0, 1
List = []
for i in range(1, N):
    if P[i-1]<P[i]:
        l+=1
    else:
        if l>=K:
            List.append(s)
        l = 1
        s = i
if l>=K:
    List.append(s)
if len(List)>0:
    s = List[0]
    for i in List[1:]:
        U.unite(s, i)
ans = 0
for i in range(N):
    if U.parent[i] == i:
        ans+=1

print(ans-K+1)
