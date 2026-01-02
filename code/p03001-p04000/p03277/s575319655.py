from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += (i & -i)

    def reset(self):
        self.bit = [0] * (self.size + 1)


BIT = BinaryIndexedTree(2 * N + 1)  # N+1番目が真ん中
target = (N * (N+1) // 2 + 1) // 2

# にぶたん
l, r = -1, 10**9+1

while r - l > 1:
    X = (r + l) // 2
    Binary = [(1 if a > X else -1) for a in A]
    Binary = list(accumulate(Binary))

    BIT.reset()

    inversion = 0

    for j in range(N):
        inversion += BIT.sum(Binary[j] + N + 1) + (Binary[j] >= 0)
        BIT.add(Binary[j] + N + 1, 1)

    if inversion >= target:
        l = X
    else:
        r = X

print(r)
