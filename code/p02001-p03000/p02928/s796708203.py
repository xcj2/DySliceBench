from collections import Counter


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


n, k = map(int, input().split())
aaa = list(map(int, input().split()))
MOD = 10 ** 9 + 7
bit = Bit(2001)
single = 0
for a in reversed(aaa):
    single += bit.sum(a)
    bit.add(a + 1, 1)
ans = single * k % MOD
coef = k * (k - 1) // 2 % MOD
cnt = Counter(aaa)
before = 0
for a, c in sorted(cnt.items()):
    ans = (ans + c * before * coef) % MOD
    before += c
print(ans)
