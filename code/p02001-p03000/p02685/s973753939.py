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

    def multi_choose(self, n, r):
        """重複組み合わせ nHr """
        return self.combination(n - 1 + r, r)

    def factorial(self, n):
        return self.fact[n]


def main():
    MOD = 998244353

    N, M, K = map(int, input().split())

    mp = [1]
    t = 1
    for _ in range(N):
        t = t * (M - 1) % MOD
        mp.append(t)

    calc = Calc(max_value=N, mod=MOD)

    ans = mp[N - 1]
    for i in range(1, K + 1):
        ans = (ans + mp[N - 1 - i] * calc.combination(N - 1, i)) % MOD
    ans = ans * M % MOD
    print(ans)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
#
# sys.setrecursionlimit(10 ** 7)
#
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
