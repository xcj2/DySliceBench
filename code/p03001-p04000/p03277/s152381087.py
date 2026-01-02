from itertools import accumulate


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

    def reset(self):
        self.tree = [0] * (self.size + 1)


def solve(n, aaa):
    t = n * (n + 1) // 4
    alt = sorted(set(aaa))
    l, r = 0, len(alt) - 1
    bt = Bit(n * 2)
    while l <= r:
        m = (l + r) // 2
        am = alt[m]
        ccc = accumulate(1 if a - am >= 0 else -1 for a in aaa)
        bt.add(n, 1)
        right_order = 0
        for p in ccc:
            p += n
            right_order += bt.sum(p)
            bt.add(p, 1)
        if right_order >= t:
            l = m + 1
        else:
            r = m - 1
        bt.reset()
    return alt[r]


n = int(input())
aaa = list(map(int, input().split()))
print(solve(n, aaa))
