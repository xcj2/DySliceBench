MOD = 998244353
factorial = None
inverse_factorial = None


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
    global factorial, inverse_factorial
    factorial = [1]*(max_n+1)
    inverse_factorial = [0]*(max_n+1)
    for i in range(1, max_n+1):
        factorial[i] = (factorial[i-1]*i)%MOD
        inverse_factorial[i] = modpow(factorial[i], MOD-2)


init_nCr(2*10**5+1)


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M, K = read_ints()
    answer = 0
    for k in range(0, K+1):
        answer = (answer+M*modpow(M-1, N-1-k)*nCr(N-1, k))%MOD
    return answer


if __name__ == '__main__':
    print(solve())
