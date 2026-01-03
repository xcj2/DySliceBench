

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


factorial = [1]
modulo = 10**9+7
inverse_factorial = [0]


def pow1(a, p):
    if p == 0:
        return 1
    half = pow1(a, p//2)
    total = (half*half)%modulo
    if p%2 == 0:
        return total
    return (total*a)%modulo


def modpow(a, p):
    ans = 1
    while p:
        if p&1 == 1:
            ans = (ans*a)%modulo
        a = (a*a)%modulo
        p >>= 1
    return ans


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return (((factorial[n]*inverse_factorial[n-r])%modulo)*inverse_factorial[r])%modulo


def solve():
    """
    2 3 1 1
    ...
    x..  A

    B

    C(2, 1)*C(3, 2)

    m 0 n 1 C(m, n) 1
    m 1 n 2 C(m, n) 2
    m 0 n 2 C(m, n) 4
    m 1 n 3 C(m, n) 12
    """
    H, W, A, B = read_ints()
    for i in range(1, H+W):
        f = (factorial[-1]*i)%modulo
        factorial.append(f)
        inv_f = modpow(f, modulo-2)
        inverse_factorial.append(inv_f)
    T = 0
    for d in range(B, W):
        # d = 0, 1
        y0 = d
        x0 = H-A-1
        y1 = W-d-1
        x1 = A-1
        T = (T+(nCr(x0+y0, x0)*nCr(x1+y1, x1))%modulo)%modulo
    return T


if __name__ == '__main__':
    print(solve())
