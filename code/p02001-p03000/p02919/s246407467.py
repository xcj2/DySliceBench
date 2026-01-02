import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)
        self.size = size

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

N = int(input())
P = list(map(int, input().split()))
idx = [-1] * (N+1)
for i, p in enumerate(P):
    idx[p] = i + 1
bit = BIT(N+1)
bit.add(0, 1)
ans = 0

def bin_search(target):
    lb, ub = -1, N+1
    while ub - lb > 1:
        m = (lb + ub) // 2
        if bit.sum(m) < target:
            lb = m
        else:
            ub = m
    return ub

for p in range(1, N+1)[::-1]:
    c = idx[p]
    s = bit.sum(c)
    a = bin_search(s-1)
    b = bin_search(s)
    d = bin_search(s+1)
    e = bin_search(s+2)
    ans += p * ((b-a) * (d-c) + (c-b) * (e-d))
    bit.add(c, 1)
print(ans)
