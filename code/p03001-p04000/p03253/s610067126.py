N, M = [int(_) for _ in input().split()]

mod = 10 ** 9 + 7
MAX_N = 10 ** 5 + 100

#階乗
def calc_factorial(max_i):
    factorial = [1] * max_i
    for i in range(1, max_i):
        factorial[i] = (i * factorial[i - 1]) % mod
    return factorial

#素因数分解
def calc_factorization(n):
    factorization = {}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factorization[i] = 1
            n = n // i
            while n % i == 0:
                factorization[i] += 1
                n = n // i
    if n > 1:
        factorization[n] = 1
    return factorization

#組み合わせ
def comb(factorial, n, k, mod):
    a = factorial[n] % mod
    b = (factorial[k] * factorial[n - k]) % mod
    b_ = pow(b, mod - 2, mod)
    return (a * b_) % mod

C = calc_factorization(M)
#階乗を計算しておく
factorial = calc_factorial(MAX_N)

res = 1
for c in C.items():
    res *= comb(factorial, (c[1] + N - 1), c[1], mod) #combinations_count(factorial, (c[1] + N - 1), c[1], mod)

print(res % mod)