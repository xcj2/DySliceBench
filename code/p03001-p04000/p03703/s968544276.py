from itertools import accumulate
import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)
        self.size = size

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
cum = list(accumulate([0] + a))
v = [cum[i] - K*i for i in range(N+1)]
vs = list(set(v))
vs.sort()
compress = {vs[i]: i for i in range(len(vs))}
bit = BIT(len(vs))
ans = 0
for i in range(N+1):
    x = compress[v[i]]
    ans += bit.sum(x)
    bit.add(x, 1)
print(ans)