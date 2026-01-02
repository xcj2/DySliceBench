def main():
    def nCk(n, k, mod=10 ** 9 + 7):
        def xgcd(a, b):
            if b == 0:
                return (1, 0)
            x, y = xgcd(b, a % b)
            return (y, x - (a // b) * y)
        p, q = 1, 1
        for i in range(n - k + 1, n + 1):
            p = (p * i) % mod
        for i in range(2, k + 1):
            q = (q * i) % mod
        return p * (xgcd(q, mod)[0] % mod) % mod


    X, Y = map(int, input().split())

    b = (2 * X - Y) // 3
    a = (-X + 2 * Y) // 3

    if (X + Y) % 3 != 0 or a < 0 or b < 0:
        print(0)
    else:
        print(nCk(a + b, a))

main()
