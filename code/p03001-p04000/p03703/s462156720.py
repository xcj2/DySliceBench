from itertools import accumulate
from bisect import bisect_right

class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i
            
N, K = map(int, input().split())
a = [int(input()) - K for _ in range(N)]
b = [0]+list(accumulate(a))
b_sorted = sorted(b)
b = [bisect_right(b_sorted, bi) for bi in b]
bit = BIT(N+1)
ans = 0
for i in range(N+1):
    ans += bit.sum(b[i])
    bit.add(b[i], 1)
print(ans)