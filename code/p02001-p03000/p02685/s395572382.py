import sys
def input():
    return sys.stdin.readline().rstrip('\n')

Z = 998244353


class Comb:
    def __init__(self, n):
        self.n = n
        self.e = [1] * (n + 1)
        for j in range(n):
            self.e[j + 1] = (self.e[j] * (j + 1)) % Z
    
    def z_pow(self, a, n):
        # a ^ n
        if n == 0:
            return 1
        if n == 1:
            return a % Z
        m = n // 2
        i = n - m * 2
        x = self.z_pow(a, m)
        return (x * x * self.z_pow(a, i)) % Z

    def get(self, i):
        if self.n - i < i:
            return self.get(self.n - i)
        return (self.e[self.n] * self.z_pow(self.e[i], Z - 2) * self.z_pow(self.e[self.n - i], Z - 2)) % Z


def calc(N, M, K):
    comb = Comb(N - 1)
    p = (M * (M - 1) ** (N - 1 - K)) % Z
    r = 0
    for x in range(K, -1, -1):
        r = (r + comb.get(x) * p) % Z
        p = (p * (M - 1)) % Z
    return r
    

(N, M, K) = tuple([int(s) for s in input().split()])
print(calc(N, M, K))