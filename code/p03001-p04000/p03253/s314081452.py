import math

def prime_factor2(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors

def kai(n):
    return math.factorial(n)

def H(n, r):
    rtn = 1
    for i in range(n+r-1, n-1, -1):
        rtn *= i
    rtn //= kai(r)
    return rtn


N, M = map(int, input().split())

prime = prime_factor2(M)

ans = 1
mili = (10**9 + 7)
for v in prime.values():
    h = H(N, v) % mili
    ans  =  ans * h

ans = ans % mili
ans = int(ans)
print(ans)