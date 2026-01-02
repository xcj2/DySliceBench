# coding:utf-8

INF = float('inf')
MOD = 10 ** 9 + 7


def inpl(): return list(map(int, input().split()))


class RollingHash:
    def __init__(self, s, base, mod):
        self.s = s
        self.length = length = len(s)
        self.base = base
        self.mod = mod
        self.h = h = [0] * (length + 1)
        for i in range(length):
            h[i + 1] = (h[i] * base + ord(s[i])) % mod
        self.p = p = [1] * (length + 1)
        for i in range(length):
            p[i + 1] = pow(base, i + 1, mod)

    def get(self, l, r):
        mod = self.mod
        # return (self.h[r] - self.h[l] * pow(self.base, r - l, mod) + mod) % mod
        return ((self.h[r] - self.h[l] * self.p[r - l]) + mod) % mod


def solve():
    N, M = inpl()
    S = input()
    h1 = RollingHash(S, 13, MOD)
    h2 = RollingHash(S, 17, MOD)
    left, right = 0, 1
    vs = set()
    ans = 0
    for i in range(M):
        q = input()
        if q == 'R++':
            right += 1
        elif q == 'R--':
            right -= 1
        elif q == 'L++':
            left += 1
        else:
            left -= 1

        v = (h1.get(left, right), h2.get(left, right))
        if v not in vs:
            ans += 1
            vs.add(v)

    return ans


print(solve())

