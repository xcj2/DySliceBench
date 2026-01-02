from functools import reduce

def factorize(n):
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

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def gcd_base(x, y):
    if x % y:
        return gcd_base(y, x%y)
    return y

def gcd(numbers):
    return reduce(gcd_base, numbers)

def lcm_base(x, y):
    res = (x * y) // gcd_base(x, y)
    return res #if res <= 1000000007 else 0 #1000000007を超える場合は0

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
a = [int(i) for i in input().split()]
print(lcm(a))
