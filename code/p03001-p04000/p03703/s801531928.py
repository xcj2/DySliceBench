n, k = map(int, input().split())
A = [int(input()) for i in range(n)]
A = [a-k for a in A]

from itertools import accumulate
C = [0]+A
C = list(accumulate(C))
#print(C)

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(self.n+1) # 1-indexed

    def init(self, init_val):
        for i, v in enumerate(init_val):
            self.add(i, v)

    def add(self, i, x):
        i += 1 # to 1-indexed
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i, j):
        # return sum of [i, j)
        return self._sum(j) - self._sum(i)

    def _sum(self, i):
        # return sum of [0, i)
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

B = list(set(C))
B.sort(reverse=True)
D = {}
for i, b in enumerate(B):
    D[b] = i

C = [D[c] for c in C]
bit = BIT(max(C)+1)
ans = 0
for c in C:
    ans += bit.sum(c, bit.n)
    bit.add(c, 1)
print(ans)