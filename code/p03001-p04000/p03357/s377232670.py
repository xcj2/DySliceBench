import sys
from itertools import accumulate
readline = sys.stdin.readline

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

N = int(readline())
W = [0]*N
B = [0]*N
for i in range(1, 2*N+1):
    c, a = readline().split()
    if c == 'W':
        W[int(a)-1] = i
    else:
        B[int(a)-1] = i

cw = [0]*(N+1)
cb = [0]*(N+1)
T = BIT(2*N)
for i in range(N):
    cw[i+1] = i-T.get(W[i])
    T.add(W[i], 1)
T = BIT(2*N)
for i in range(N):
    cb[i+1] = i-T.get(B[i])
    T.add(B[i], 1)

invw = [None] + [[0] + list(accumulate([1 if W[i] < B[j] else 0 for j in range(N)])) for i in range(N)]
invb = [None] + [[0] + list(accumulate([1 if B[i] < W[j] else 0 for j in range(N)])) for i in range(N)]
    
inf = 10**9+7
dp = [[inf]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
for s in range(2*N):
    for w in range(max(0, s-N), min(N+1, s+1)):
        b = s-w
        if w != N:
            dp[w+1][b] = min(dp[w+1][b], dp[w][b] + invw[w+1][b] + cw[w+1])
        if b != N:
            dp[w][b+1] = min(dp[w][b+1], dp[w][b] + invb[b+1][w] + cb[b+1])
print(dp[N][N])