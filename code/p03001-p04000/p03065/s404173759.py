def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a%b
    return b

def divisor(a):
    i = 1
    divset = set()
    while i * i <= a:
        if a % i == 0: divset |= {i, a//i}
        i += 1
    divset.remove(1)
    return divset

def is_prime(a):
    if a <= 3: 
        prime = [False, False, True, True]
        return prime[a]
    i = 2
    while i * i <= a:
        if a % i == 0: return False
        i += 1
    else: return True

N = int(input())
A = [None] * (N+1)
for i in reversed(range(N+1)):
    A[i] = int(input())

primes_bool = [True] * (N + 1)
primes = []
for p in range(2, N+1):
    if primes_bool[p]:
        primes.append(p)
        p_mult = p * 2
        while p_mult <= N:
            primes_bool[p_mult] = False
            p_mult += p

ans = []
used = set()
gcd_of_A = abs(A[N])
for a in A[:N]:
    if a != 0: gcd_of_A = gcd(abs(a), gcd_of_A)

commondiv = divisor(gcd_of_A)
for d in commondiv:
    if d > 1 and is_prime(d): 
        ans.append(d)
        used |= {d}

for p in primes:
    if A[0] % p == 0:
        for i in range(1, p):
            coefficient = 0
            index_a = i
            while index_a <= N:
                coefficient += A[index_a]
                coefficient %= p
                index_a += p-1
            if coefficient > 0: break
        else:
            if p not in used: ans.append(p)

ans.sort()
for a in ans: print(a)
