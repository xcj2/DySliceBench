class Calc:
    def __init__(self, max_value, mod):
        """combination(max_value, all)"""
        fact = [-1] * (max_value + 1)
        fact[0] = 1
        fact[1] = 1
        for x in range(2, max_value + 1):
            fact[x] = x * fact[x - 1] % mod

        invs = [1] * (max_value + 1)
        invs[max_value] = pow(fact[max_value], mod - 2, mod)
        for x in range(max_value - 1, 0, -1):
            invs[x] = invs[x + 1] * (x + 1) % mod

        self.fact = fact
        self.invs = invs
        self.mod = mod

    def combination(self, n, r):
        if n - r < r:
            return self.combination(n, n - r)
        if r < 0:
            return 0
        if r == 0:
            return 1
        if r == 1:
            return n
        return self.fact[n] * self.invs[r] * self.invs[n - r] % self.mod

    def factorial(self, n):
        return self.fact[n]


def main():
    mod = 10 ** 9 + 7

    n, k = map(int, input().split())

    mi = min(k, n - 1)

    cl = Calc(max_value=n * 2 - 1, mod=mod)

    ret = 0
    for r in range(mi + 1):
        ret += cl.combination(n - 1, n - r - 1) * cl.combination(n, r)
        ret %= mod

    print(ret)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
