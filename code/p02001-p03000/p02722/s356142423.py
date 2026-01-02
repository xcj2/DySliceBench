from collections import defaultdict
from math import gcd

def is_prime_miller_rabin(n):  # ミラー-ラビン素数判定法
    if n < 2:
        return False
    elif n in {2, 3, 5, 7, 11}:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        return False

    if n < 4_759_123_141:
        witnesses = [2, 7, 61]
    elif n < 341_550_071_728_321:
        witnesses = [2, 3, 5, 7, 11, 13, 17]
    else:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    d = n - 1
    d = d // (d & -d)

    for a in witnesses:
        y = pow(a, d, n)
        if y == 1:
            continue
        t = d
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1:
                return False
            t <<= 1
    return True

def find_factor_rho(n):  # ポラード・ロー素因数分解法
    if n < 2:
        return None
    m = 1<<n.bit_length() // 8 + 1
    for c in range(1, 99):
        def f(x):
            return (x * x + c) % n

        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if is_prime_miller_rabin(g):
                return g
            elif is_prime_miller_rabin(n // g):
                return n // g
    return None

def prime_factorize_dict(n):
    prime_dict = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            prime_dict[i] += 1
        i += 1 + i % 2
        if i != 101 or n < 1<<20:
            continue
        while n > 1:
            if is_prime_miller_rabin(n):
                prime_dict[n] = n = 1
                break
            j = find_factor_rho(n)
            while n % j == 0:
                n //= j
                prime_dict[j] += 1
    if n > 1:
        prime_dict[n] += 1
    return prime_dict

# ---------------------- #

n = int(input())
ans = 1
for value in prime_factorize_dict(n - 1).values():
    ans *= value + 1
ans -= 1  # 1を除くn-1の約数の数

def get_divisors(n):
    lower_divisors = []
    upper_divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lower_divisors.append(i)
            if n // i != i:
                upper_divisors.append(n // i)
    return lower_divisors + upper_divisors[::-1]

for divisor in get_divisors(n)[1:]:
    tmp = n
    while tmp % divisor == 0:
        tmp //= divisor
    if tmp % divisor == 1:
        ans += 1

print(ans)
