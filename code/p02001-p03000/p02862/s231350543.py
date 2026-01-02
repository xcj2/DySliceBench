Z = 10 ** 9 + 7


def z_pow(a, n):
    # a ^ n
    if n == 0:
        return 1
    if n == 1:
        return a % Z
    m = n // 2
    i = n - m * 2
    x = z_pow(a, m)
    return (x * x * z_pow(a, i)) % Z


def n_comb(n, i):
    if n - i < i:
        return n_comb(n, n - i)
    e = [1 for j in range(n + 1)]
    for j in range(n):
        e[j + 1] = (e[j] * (j + 1)) % Z
    return (e[n] * z_pow(e[i], Z - 2) * z_pow(e[n - i], Z - 2)) % Z


def calc(X, Y):
    if (X + Y) % 3 != 0:
        return 0
    n = (X + Y) // 3
    if X < n or Y < n:
        return 0
    return n_comb(n, X - n)


(X, Y) = tuple([int(s) for s in input().split()])
print(calc(X, Y))