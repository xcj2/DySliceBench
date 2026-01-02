import math


class Solution:

    def solve(self, N: int, M: int) -> int:

        mod = 10**9+7
        INT_MAX = 10**9

        # calculate {m+n}C{n}

        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                g, y, x = egcd(b % a, a)
                return g, x - (b // a) * y, y

        def modinv(a, m):
            g, x, y = egcd(a, m)
            if g != 1:
                raise Exception('modular inverse does not exist')
            else:
                return x % m

        def combination(n: int, r: int, mod: int = 10**9+7) -> int:
            r = min(r, n-r)
            res = 1
            for i in range(r):
                res = res * (n-i) * modinv(i+1, mod) % mod
            return res

        # solve

        m = M
        answer = 1
        factors = {}
        for i in range(2, int(math.sqrt(M))+1):
            factor = 0
            while m % i == 0:
                m //= i
                factor += 1

            if factor > 0:
                answer *= combination(N + factor - 1, N - 1, mod=mod)
                answer %= mod

        if m > 1:
            answer *= N
            answer %= mod

        return answer


if __name__ == '__main__':

    # standard input
    N, M = map(int, input().split())

    # solve
    solution = Solution()
    print(solution.solve(N, M))
