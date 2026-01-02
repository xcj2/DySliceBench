def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors


def is_prime(p):
    if p == 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True


A, B = map(int, input().split())

g = gcd(A, B)
d = make_divisors(g)

ans = 1
for i in d:
    if is_prime(i):
        ans += 1

print(ans)