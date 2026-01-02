from collections import defaultdict


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s = (s + self.tree[i]) % 1000000007
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = (self.tree[i] + x) % 1000000007
            i += i & -i


n, m = list(map(int, input().split()))
sss = list(map(int, input().split()))
ttt = list(map(int, input().split()))

sid = defaultdict(list)
for i, s in reversed(list(enumerate(sss))):
    sid[s].append(i)

bit = Bit(n + 1)
bit.add(1, 1)

for t in ttt:
    if t not in sid:
        continue
    for i in sid[t]:
        bit.add(i + 2, bit.sum(i + 1))

print(bit.sum(n + 1))
