# ----------------------------- #
def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

# ----------------------------- #
def is_prime_or_one(n):
    if n == 1: return True
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True

# ----------------------------- #
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

# ----------------------------- #
a, b = [int(_) for _ in input().split()]

GCD = gcd(a, b)  # 最大公約数
DV = make_divisors(GCD)  # 公約数

cnt = 0
for i in range(len(DV)):
    cnt += is_prime_or_one(DV[i])
print(cnt)