class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

    def sum(self, i):  # sum in [0, i]
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


class BitImos:
    """
    ・範囲すべての要素に加算
    ・ひとつの値を取得
    の2種類のクエリをO(logn)で処理
    """
    def __init__(self, n):
        self.bit = Bit(n+1)

    def add(self, s, t, x):
        # [s, t)にxを加算
        self.bit.add(s, x)
        self.bit.add(t, -x)

    def get(self, i):
        return self[i]

    def __getitem__(self, key):
        # 位置iの値を取得
        return self.bit.sum(key)


N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(K)]

bit = BitImos(N+2)
bit.add(1, 2, 1)

mod = 998244353

for i in range(1, N+1):
    cur = bit.get(i) % mod
    for l, r in LR:
        if i + l > N:
            continue
        bit.add(i+l, min(i + r + 1, N + 2), cur)

print(bit.get(N) % mod)
