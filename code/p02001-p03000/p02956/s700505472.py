import sys

class BIT:
    #1-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.p = 2**(n.bit_length() - 1)
        self.dep = n.bit_length()
    
    def get(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def bl(self, v):
        if v <= 0:
            return -1
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.tree[s+k] < v:
                s += k
                v -= self.tree[s+k]
            k //= 2
        return s + 1

def compress(L):
    L2 = list(set(L))
    L2.sort()
    C = {v : k for k, v in enumerate(L2, 1)}
    return L2, C

N = int(input())
mod = 998244353
ans = N*pow(2, N-1, mod)%mod

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
points.sort()
_, PY = map(list, zip(*points))
_, Ci = compress(PY)
PY = [Ci[p] for p in PY]
T1 = BIT(N)
T2 = BIT(N)

for i in range(1, N+1):
    T2.add(i, 1)

for i in range(N):
    y = PY[i]
    c = T1.get(y)
    d = T2.get(y)-1 - c
    a = i - c
    b = N-1 - a - c - d
    T1.add(y, 1)
    a2 = pow(2, a, mod)
    b2 = pow(2, b, mod)
    c2 = pow(2, c, mod)
    d2 = pow(2, d, mod)
    ans += (a2-1)*b2*c2*(d2-1) + a2*(b2-1)*(c2-1)*d2 - (a2-1)*(b2-1)*(c2-1)*(d2-1)
    ans %= mod
print(ans)