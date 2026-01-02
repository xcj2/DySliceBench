def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)


def make_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.append(n)
    return divisors


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


A, B = map(int, input().split())

C = gcd(A, B)

d = prime_factorize(C)
d.append(1)

print(len(list(set(d))))
