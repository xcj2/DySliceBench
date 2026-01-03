from bisect import bisect_left


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

    def sum(self, i):  # [0, i)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):  # i > 0
        assert i > 0
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

d = [0] * (n+1)
d2 = {0}
for i in range(n):
    d[i+1] = d[i] + a[i] - k
    d2.add(d[i+1])

d2 = sorted(d2)

bit = Bit(len(d2))

ans = 0
for i in range(n+1):
    d2_i = bisect_left(d2, d[i])
    ans += bit.sum(d2_i+1)
    bit.add(d2_i+1, 1)

print(ans)
