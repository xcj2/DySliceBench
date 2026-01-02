import bisect
import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
co = []
for i in range(n):
    co.append(na())
    co[-1][1] += co[-1][0]
co.sort(key=lambda x: x[0])


class Segtreermq:
    def __init__(self, n):
        self.H = 1
        while self.H < n:
            self.H *= 2
        self.M = self.H * 2
        self.vals = [999999999999] * self.M

    def update(self, pos, v):
        self.vals[self.H+pos] = v
        x = self.H+pos>>1
        while x >= 1:
            self.vals[x] = min(self.vals[2*x], self.vals[2*x+1])
            x>>=1

    def min(self, l, r):
        ret = 999999999999999
        if l >= r:
            return ret
        while l != 0:
            f = l&-l
            if l+f > r:
                break
            v = self.vals[(self.H+l)//f]
            if v < ret:
                ret = v
            l += f

        while l < r:
            f = r & -r
            v = self.vals[(self.H+r)//f-1]
            if v < ret:
                ret = v
            r -= f
        return ret

xs = [_[0] for _ in co]

st = Segtreermq(n)
for i in range(n-1,-1,-1):
    ind = bisect.bisect_left(xs, co[i][1])
    reach = max(co[i][1], -st.min(i, ind))
    st.update(i, -reach)
    co[i][1] = reach

mod = 998244353
stack = []
dp = [0] * n
for i in range(n-1,-1,-1):
    val = 1
    while len(stack) > 0 and co[stack[-1]][1] <= co[i][1]:
        val = val * dp[stack[-1]] % mod
        stack.pop(-1)
    dp[i] = (val + 1) % mod
    stack.append(i)

ans = 1
for s in stack:
    ans = ans * dp[s] % mod
print(ans)
