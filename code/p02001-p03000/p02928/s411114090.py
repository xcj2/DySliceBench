N, K = map(int, input().split())
A = list(map(int, input().split()))


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


def inversion(a):
    "転倒数を求める"
    d = {av: i+1 for i, av in enumerate(sorted(a))}
    b = Bit(len(a))
    ans = 0
    for i, av in enumerate(a):
        ans += i-b.sum(d[av])
        b.add(d[av], 1)
    return ans


MOD = 10**9+7
L = len(set(A))

count = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            count += 1
ans = (inversion(A) * K) % MOD + (K*(K-1)//2) * count % MOD
ans %= MOD
print(ans)
