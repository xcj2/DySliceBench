import sys
input = sys.stdin.readline

class RangeUpdateQuery:
    def __init__(self, n):
        self.n0 = 2**(n-1).bit_length()
        self.INF = float("inf")
        self.data = [self.INF]*(2*self.n0-1)

    def update(self, l,r,v):
        l += self.n0
        r += self.n0
        while l < r:
            if r&1:
                r -= 1
                self.data[r-1] = v
            if l&1:
                self.data[l-1] = v
                l += 1
            l >>=1
            r >>=1

    def query(self, i):
        i += self.n0-1
        res = self.INF
        while i+1:
            if self.data[i] < res:
                res = self.data[i]
            i = ~-i//2
        return res

n,q = map(int, input().split())
start = [None]*q
se = set()

road = []
for i in range(n):
    s,t,x = map(int, input().split())
    road.append([x, x-t, x-s])
for i in range(q):
    d = int(input())
    start[i] = -d

start = start[::-1]

RUQ = RangeUpdateQuery(q)
road.sort(reverse=True)
from bisect import bisect_left,bisect_right
for i, (x, s, t) in enumerate(road):
    l = bisect_right(start, s)
    r = bisect_right(start, t)
    #print(x, (s,t), l, r)
    RUQ.update(l, r, x)

ans = []
for i in range(q):
    x = RUQ.query(i)
    if x == float("inf"):
        x = -1
    ans.append(x)
ans = ans[::-1]
print(*ans, sep="\n")