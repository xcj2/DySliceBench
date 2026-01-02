# 素因数分解
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

# nの約数のlist
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


# 素数判定
def is_prime(q):
    q = abs(q)
    if q == 2:
        return True
    if q < 2 or q & 1 == 0:
        return False
    return pow(2, q-1, q) == 1


a, b = map(int, input().split())
d_a = set(prime_factorize(a))
d_b = set(prime_factorize(b))
matched_list = list(d_a & d_b)
matched_list.sort()

count = 0

for i in matched_list:
    if is_prime(i):
        count += 1

print(count+1)
