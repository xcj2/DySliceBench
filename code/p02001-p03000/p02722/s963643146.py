from collections import Counter
from itertools import product


from functools import reduce
import operator
nproduct = lambda it: reduce(operator.mul,it,1)

# 素因数分解
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

def all_divisors(n):
    factors,counts = map(tuple,zip(*Counter(prime_factors(n)).items()))

    for p in product(*(range(c+1) for c in counts)):
        yield nproduct(v**k for v,k in zip(factors,p))

def num_divisors(n):
    return nproduct(c+1 for c in Counter(prime_factors(n)).values())


N = int(input())

cnt = num_divisors(N-1)
for d in all_divisors(N):
    if d == 1:
        continue
    x = N
    while x % d == 0:
        x //= d
    if x % d == 1:
        cnt += 1

print(cnt-1)