from collections import defaultdict
from math import sqrt
inpl = lambda: list(map(int,input().split()))
 
def primes(N):
    P = []
    for i in range(2,N):
        sieve = 1
        for p in P:
            if p*p > i:
                break
            elif i % p == 0:
                sieve = 0
                break
        if sieve == 0:
            continue
        else:
            P.append(i)
    return P
 
def factorize(n, P=None):
    if P is None:
        P = primes(int(sqrt(n))+1)
    factor = []
    power = []
    for p in P:
        if p * p > n:
            break
        elif n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            factor.append(p)
            power.append(k)
    if n > 1:
        factor.append(n)
        power.append(1)
    return factor, power
 
class Counter:
    def __init__(self, start=0):
        self.index = start-1
 
    def __call__(self):
        self.index += 1
        return self.index
 
N = int(input())
A = inpl()
 
P_MAX = 32000
infty = 100
P = primes(P_MAX)
 
np = defaultdict(Counter())
Np = 0
 
lowest_powers = []
bottle_necks = []
primelist = []
all_factors = set()
for n in range(N):
    primes, powers = factorize(A[n],P)
    pp = [0]*Np
    for i in range(len(primes)):
        k = np[primes[i]]
        if k >= Np:
            Np += 1
            pp.append(powers[i])
            primelist.append(primes[i])
            if n > 1:
                lowest_powers.append([0,0])
                bottle_necks.append(-1)
            elif n == 1:
                lowest_powers.append([0,infty])
                bottle_necks.append(0)
            else:
                lowest_powers.append([infty,infty])
                bottle_necks.append(-1)
        else:
            pp[k] = powers[i]
    for k in range(Np):
        lowest = lowest_powers[k]
        if pp[k] == lowest[0]:
            lowest[1] = lowest[0]
            bottle_necks[k] = -1
        elif pp[k] < lowest[0]:
            lowest[1] = lowest[0]
            lowest[0] = pp[k]
            bottle_necks[k] = n
        elif pp[k] < lowest[1]:
            lowest[1] = pp[k]
 
bottleneck_factors = [ [] for _ in range(N) ]
for k in range(Np):
    n = bottle_necks[k]
    if n >= 0:
        lowest = lowest_powers[k]
        bottleneck_factors[n].append([primelist[k],lowest[1]-lowest[0]])
best_n = -1
largest_f = 1
for n in range(N):
    f = 1
    for pp in bottleneck_factors[n]:
        f *= pp[0]**pp[1]
    if f > largest_f:
        largest_f = f
        best_n = n
 
ans = 1
pn = [ s[0] for s in bottleneck_factors[best_n] ]
for k in range(Np):
    p = primelist[k]
    if bottle_necks[k] == best_n:
        ans *= p**lowest_powers[k][1]
    else:
        ans *= p**lowest_powers[k][0]
print(ans)