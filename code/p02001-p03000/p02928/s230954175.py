class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    # sum[0:i+1]
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    # add x to i
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

def inv(X):
    B = Bit(2000+1)
    inv = 0
    for i in range(len(X)):
        inv += i - B.sum(X[i])
        B.add(X[i], 1)
    return inv

A_inv = inv(A) % MOD
A2_inv = inv(A*2) % MOD

print((K*A_inv + ((K*(K-1))//2) * (A2_inv - 2*A_inv)) % MOD)