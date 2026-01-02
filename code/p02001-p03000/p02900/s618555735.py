import math

# N = int(input())
# A = list(map(int, input().split()))
A, B = map(int, input().split())


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def is_prime(n):
    if n == 1:
        return True

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


print(sum([is_prime(n) for n in make_divisors(gcd(A, B))]))
