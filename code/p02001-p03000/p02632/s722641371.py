

MOD = 10**9+7
factorial = [1]
inverse_factorial = [0]


def modpow(a, p):
    ans = 1
    while p:
        if p&1 == 1:
            ans = (ans*a)%MOD
        a = (a*a)%MOD
        p >>= 1
    return ans


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return (((factorial[n]*inverse_factorial[n-r])%MOD)*inverse_factorial[r])%MOD


def init_nCr(max_n):
    for i in range(1, max_n+1):
        f = (factorial[-1]*i)%MOD
        factorial.append(f)
        inv_f = modpow(f, MOD-2)
        inverse_factorial.append(inv_f)


def pow(b, p):
    ans = 1
    for _ in range(p):
        ans = (ans*b)%MOD
    return ans


def pow_list(b, p):
    ans = [1]
    for _ in range(p):
        ans.append((ans[-1]*b)%MOD)
    return ans


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    K = read_int()
    S = len(input().strip())
    init_nCr(K+S)
    T = pow(26, K+S)
    pow_25 = pow_list(25, K+S)
    for i in range(S):
        T = (T-(nCr(K+S, i)*pow_25[K+S-i])%MOD)%MOD
    return T


if __name__ == '__main__':
    print(solve())
