n, a, b, k = map(int, input().split())

M = 998244353
fact_n = [0 for m in range(n+1)]
fact_inv = [0 for m in range(n+1)]


def mod_pow(a, n):
    x = 1
    while n > 0:
        if n & 1:
            x = x * a % M

        a = a * a % M
        n >>= 1

    return x


def combination(n, r):
    if n == 0 and r == 0:
        return 1
    elif n < r or n < 0:
        return 0

    return fact_n[n] * fact_inv[r] * fact_inv[n-r] % M


def main():
    fact_n[0] = fact_inv[0] = 1
    for i in range(1, n+1):
        fact_n[i] = fact_n[i-1] * i % M

    fact_inv[n] = pow(fact_n[n], M-2, M)
    for i in range(n-1, 0, -1):
        fact_inv[i] = fact_inv[i+1] * (i+1) % M

    com = 0
    for i in range(n+1):
        if (k-a*i) % b == 0 and k - a * i >= 0:
            j = (k-a*i) // b
            com += combination(n, i) * combination(n, j) % M

    print(com % M)


if __name__ == '__main__':
    main()
