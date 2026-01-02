A, B = map(int, input().split())

import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1

    return lower_divisors + upper_divisors[::-1]


def gcd(a, b):

    if a == 0:
        return b
    else:
        return gcd(b%a, a)


da = make_divisors(A)
common_divisors = []

for d in da:
    if B % d == 0:
        common_divisors.append(d)

ans = [1 if is_prime(x) else 0 for x in common_divisors]
print(sum(ans))
