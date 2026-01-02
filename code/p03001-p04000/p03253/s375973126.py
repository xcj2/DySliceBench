import math
import collections
def main():
    N, M = map(int, input().split())
    mod = pow(10, 9) + 7
    if M == 1: return 1

    ps = factorize(M)
    K = max(ps.values())

    pow1 = [1, 1]
    for i in range(2, N+K+1):
        pow1.append(pow1[-1]*i % mod)

    ref = powerquick(pow1[-1], mod-2, mod) # ((N+K)!)^-1 % mod
    invpow1 = [ref]
    for i in range(N+K, 0, -1):
        invpow1.append(invpow1[-1]*i % mod)
    invpow1 = invpow1[::-1]

    # for i in range(len(pow1)):
    #     print(pow1[i]*invpow1[i] % mod)
    # print(invpow1)
    # print(pow1)

    ans = 1
    for p in ps:
        l = ps[p]
        v = pow1[l+N-1]*invpow1[N-1]*invpow1[l] % mod
        ans = (ans * v) % mod

    # print(factorize(35))
    return ans
    # if M == 1: return 1

def powerquick(x, y, mod):
    if y == 0: return 1
    if y == 1: return x % mod
    if y % 2 == 0:
        return pow(powerquick(x, y//2, mod), 2) % mod
    else:
        return pow(powerquick(x, y//2, mod), 2) * x % mod


def factorize(n):
    ps = collections.defaultdict(int)
    if n == 1: return ps
    if isPrime(n):
        ps[n] += 1
        return ps

    p = 1
    while n > 1:
        while not isPrime(p):
            p += 1
        count = 0
        while n % p == 0:
            count += 1
            n = n // p
        if count > 0:
            ps[p] = count
            if isPrime(n):
                ps[n] += 1
                return ps
        p += 1
    return ps

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(main())