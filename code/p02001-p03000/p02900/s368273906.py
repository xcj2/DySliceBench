def gcd(a, b):
    if a < b:
        a, b = b, a
    return b if a % b == 0 else gcd(b, a%b)

MAX_NUM = 10**6
is_prime = [True] * MAX_NUM
is_prime[0] = False
is_prime[1] = False
primes = []
for i in range(2, MAX_NUM):
    if is_prime[i]:
        primes.append(i)
        for j in range(2*i, MAX_NUM, i):
            is_prime[j] = False

def f(x):
    res = {}
    for p in primes:
        if x % p == 0:
            res[p] = 0
            while x % p == 0:
                res[p] += 1
                x //= p
    if x > 1:
        res[x] = 1
    return res

def solve(a, b):
    p = f(gcd(a, b))
    return len(p) + 1

a, b = map(int, input().split())
print(solve(a, b))