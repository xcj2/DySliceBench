from itertools import accumulate
from math import ceil

N = int(input())
a = list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        
    def update(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i
            
    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret
    
    def reset(self):
        self.bit = [0] * (self.n + 1)

ub = max(a) + 1
lb = 0
th = ceil(((N + 1) * N // 2) / 2)
bit = BIT(N + 1)

while ub - lb > 1:
    mid = (ub + lb) // 2
    b = [1 if v >= mid else -1 for v in a]
    b = [0] + list(accumulate(b))
    b_sorted = {v: i + 1 for i, v in enumerate(sorted(b))}
    
    # Count inversion
    cnt = 0
    bit.reset()
    for v in b:
        cnt += bit.query(b_sorted[v])
        bit.update(b_sorted[v], 1)
        
    if cnt >= th:
        lb = mid
    else:
        ub = mid
    
print(lb)





