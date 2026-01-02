

modulo = 10**9+7

def modpow(base, n):
    ans = 1
    while n:
        if n&1:
            ans = (ans*base)%modulo
        base = (base*base)%modulo
        n >>= 1
    return ans
    

factorials = [1]
N = 10**5
for i in range(1, N+1):
    factorials.append((factorials[-1]*i)%modulo)

inv = [0]
for i in range(1, N+1):
    inv.append(modpow(factorials[i], modulo-2))


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return (factorials[n]*inv[n-r]*inv[r])%modulo


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, K = read_ints()
    A = read_ints()
    A.sort()
    max_sum = 0
    for i in range(K-1, N):
        max_sum = (max_sum+A[i]*nCr(i, K-1))%modulo
    min_sum = 0
    for i in range(N-K+1):
        min_sum = (min_sum+A[i]*nCr(N-i-1, K-1))%modulo
    return (max_sum-min_sum)%modulo


if __name__ == '__main__':
    print(solve())
