def main():
    N = int(input())

    def prime_factorize(n):
        res = []
        for i in range(2, n+1):
            if i*i > n:
                break
            if n % i != 0:
                continue
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append((i, ex))
        if n != 1:
            res.append((n, 1))
        return res

    def euler_totient_function(n):
        # オイラーのφ関数
        # 1からnのうち，nと互いに素な整数の個数
        pf = prime_factorize(n)
        res = n
        for p, _ in pf:
            res *= p-1
            res //= p
        return res

    print(euler_totient_function(N))


if __name__ == '__main__':
    main()

