from functools import reduce
MOD = 10**9+7
n = int(input())
A = list(map(int, input().split()))


def factorization(n):
    retval = []
    tmp = n
    for i in range(2, int(-(-n**.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            retval.append((i, cnt))
    if tmp != 1:
        retval.append((tmp, 1))
    return retval


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a*b)//gcd(a, b)


x = reduce(lcm, A) % MOD
print(sum(x*pow(a, MOD-2, MOD) for a in A) % MOD)
