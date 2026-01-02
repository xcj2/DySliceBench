N = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True

def insu(num):
    from collections import defaultdict
    div_prime = [d for d in make_divisors(num) if is_prime(d)]
    res = defaultdict(int)
    for d in div_prime:
        while num % d == 0:
            num //= d
            res[d] += 1
    return res
ins = insu(N)
ans = 0
for v in ins.values():
    counter = 1
    while v >= counter:
        v -= counter
        counter += 1
        ans += 1
print(ans)
