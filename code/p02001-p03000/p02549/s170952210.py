import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
mod = 998244353
dp = [0]*(N+1)
dp[1] = 1

Ks = [list(mapint()) for _ in range(K)]
Ks.sort()

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sums(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

bit = Bit(N)
bit.add(1, 1)

for i in range(2, N+1):
    for l, r in Ks:
        if i-l<0:
            break
        dp[i] += bit.sums(i-l) - bit.sums(max(0, i-r-1))
        dp[i] %= mod
    bit.add(i, dp[i])

print(dp[-1])