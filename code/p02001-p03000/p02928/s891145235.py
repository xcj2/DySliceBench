import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left


class BIT:  # 0-indexed
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.tree[0] = None

    def sum(self, i):  # a_0 + ... + a_{i} #閉区間
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range(self, l, r):  # a_l + ... + a_r 閉区間
        return sum(r) - sum(l - 1)

    def add(self, i, x):
        i += 1
        while i <= n:
            self.tree[i] += x
            i += i & -i


n, k = map(int, readline().split())
a = list(map(int, readline().split()))
s_a = sorted(a)
mod = 10 ** 9 + 7
bit = BIT(n)
res = [0] * n
ans = 0
for i, b in enumerate(a):
    j = bisect_left(s_a, b)
    res[i] = i - bit.sum(j)
    bit.add(j, 1)
for i, b in enumerate(a):
    ans += k * res[i]
    ans %= mod
    j = bisect_left(s_a, b)
    ans += (k * (k - 1) // 2 % mod) * (n - bit.sum(j))
    ans %= mod
print(ans)
