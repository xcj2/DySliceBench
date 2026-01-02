def main():
    N, M = (int(i) for i in input().split())
    from math import gcd

    def lcm(x, y):
        return x*y//gcd(x, y)

    def prime_factorize(n):
        res = {2: 0}
        for i in range(2, 3):
            if i*i > n:
                break
            if n % i != 0:
                continue
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res[i] = ex
        if n != 1:
            res[n] = 1
        return res

    B = [int(i)//2 for i in input().split()]
    c = set()
    L = 1
    for b in B:
        L = lcm(L, b)
        c.add(prime_factorize(b)[2])

    if len(c) != 1:
        print(0)
    else:
        ans = 0
        i = 1
        while L*i <= M:
            ans += 1
            i += 2
        print(ans)


if __name__ == '__main__':
    main()
