import sys
input = sys.stdin.readline


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def modInverse(a, p):
    return pow(a, p - 2, p)
def nCr(n, r, p=10**9+7):
    x = 1
    for i in range(r):
        x = (x * (n - i)) % p
    d = 1
    for i in range(1, r + 1):
        d = (d * i) % p
    return (x * modInverse(d, p)) % p


N = int(input())
import collections
A = []
for i in range(2, N+1):
    A.extend(prime_factorize(i))
P = collections.Counter(A)


def f(n):
    return len([k for k, v in P.items() if v >= n])


def main():
    ans = 0
    ans += f(74)
    ans += f(24) * (f(2)-1)
    ans += f(14) * (f(4)-1)
    ans += nCr(f(4), 2) * (f(2)-2)
    print(ans)


if __name__ == '__main__':
    main()
