import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def all_factors(n):
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small
def is_prime(n):
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

a,b=get_ints()
g=gcd(a,b)
lst=all_factors(g)
count=1
for i in lst:
    if is_prime(i):
        count+=1
print(count)