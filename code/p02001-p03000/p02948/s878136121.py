import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
c = 0
ab.sort(key = lambda x: (x[0], -x[1]))
from heapq import heappop as hpp, heappush as hp
class HST:
    def __init__(self, ascending=True):
        self._h = []
        self._q = []
        self.ascending = ascending
    def push(self, v):
        if not self.ascending:
            v *= -1
        hp(self._h, v)
    def remove(self, v):
        if not self.ascending:
            v *= -1
        hp(self._q, v)
    def top(self):
        while self._q and self._q[0]==self._h[0]:
            hpp(self._q)
            hpp(self._h)
        if not self._h:
            res = None
        else:
            res = self._h[0]
            if not self.ascending:
                res *= -1
        return res
h = HST(ascending=False)
ans = 0
ab = ab[::-1]
# print(ab)
for c in range(m, -1, -1):
    while ab and ab[-1][0]+c<=m:
        a,b = ab.pop()
        h.push(b)
    val = h.top()
    if val is not None:
        ans += val
        h.remove(val)
print(ans)