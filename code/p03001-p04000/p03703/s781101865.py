from itertools import accumulate
import bisect


class Bit():
    def __init__(self, N):
        self.size = N
        self.bit = [0] * (self.size+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self):
        return str(self.bit)


N, K = map(int, input().split())
A = [-10**9] + [int(input()) for i in range(N)]

diff = [a - K for a in A]
diff = list(accumulate(diff))
graph = Bit(N+1)
temp = sorted(diff)
order = [bisect.bisect_right(temp, d) for d in diff]
ans = 0

for x in order:
    ans += graph.sum(x)
    graph.add(x, 1)

print(ans)