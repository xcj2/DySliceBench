class Solution:
    def solve(self, x: int, y: int) -> int:

        if (2*x - y) % 3 != 0 or (-x + 2*y) % 3 != 0:
            return 0

        m = (2*x - y) // 3
        n = (-x + 2*y) // 3

        if m < 0 or n < 0:
            return 0

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

        def convination(n: int, r: int, mod: int = 10**9+7) -> int:
            r = min(r, n-r)
            res = 1
            for i in range(r):
                res = res * (n-i) * modinv(i+1, mod) % mod
            return res

        return convination(n+m, m)


if __name__ == '__main__':

    # standard input
    x, y = map(int, input().split())

    # solve
    solution = Solution()
    print(solution.solve(x, y))
