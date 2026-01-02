import math
n, m = map(int, input().split())
mod = 1000000007
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for j in range(4, n+1, 2):
        is_prime[j] = False
    for i in range(3, int(n**0.5) + 1, 2):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def nCr(n, r):
    r = min(r, n - r)
    if r == 0: return 1;
    if r == 1: return n;
    numerator = [n - r + i + 1 for i in range(r)]
    denominator  = [i + 1 for i in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1: 
            result *= numerator[k] % mod
    return result

def nHr(n, r):
    return nCr(n+r-1, r)

prime_list = prime(int(math.sqrt(m)))
divisor_list = {}
while m > 1:
    for i in prime_list:
        if m % i == 0:
            if i in divisor_list:
                divisor_list[i] = divisor_list[i] + 1
            else:
                divisor_list[i] = 1
            m = m // i
            break
        if i == prime_list[-1]:
            divisor_list[m] = 1
            m = 1
            break
ans = 1
for k in divisor_list:
    ans *= nHr(n, divisor_list[k]) % mod
    ans %= mod
print(ans)