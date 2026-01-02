import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

import sys
sys.setrecursionlimit(10**7)

class RangeMinimumQuery:
    def __init__(self, n):
        self.n0 = 2**(n-1).bit_length()
        self.data = [0]*(2*self.n0)

    def query(self, l,r):
        l += self.n0
        r += self.n0
        res = 0
        while l < r:
            if r&1:
                r -= 1
                res = max(res, self.data[r-1])
            if l&1:
                res = max(res, self.data[l-1])
                l += 1
            l >>=1
            r >>=1
        return res

    def update(self, i, x):
        i += self.n0-1
        self.data[i] = x
        while i:
            i = ~-i//2
            self.data[i] = max(self.data[2*i+1], self.data[2*i+2])


n = int(input())
a = list(map(int, input().split()))
d = {j:i for i,j in enumerate(sorted(set(a)))}
m = len(d)
a = [d[i] for i in a]

G = [[] for i in range(n)]
for i in range(n-1):
    u,v = map(int, input().split())
    u,v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

RMQ = RangeMinimumQuery(m+10)
ans = [0]*n
def dfs(cur, prev):
    ai = a[cur]
    now = RMQ.query(ai, ai+1)
    nxt = max(RMQ.query(0, ai)+1, now)
    RMQ.update(ai, nxt)
    ans[cur] = RMQ.query(0, m+1)
    for to in G[cur]:
        if to != prev:
            dfs(to, cur)
    RMQ.update(ai, now)
dfs(0,-1)

print(*ans, sep="\n")

