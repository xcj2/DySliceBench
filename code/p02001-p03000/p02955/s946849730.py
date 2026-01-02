
# 素因数分解
from collections import Counter
from itertools import product
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

from functools import reduce
import operator
int_product = lambda it: reduce(operator.mul,it,1)


def divisors(n):
    factors = prime_factors(n)
    factors = Counter(factors)
    pows = tuple(factors.values())
    factors = tuple(factors.keys())
    for pp in product(*(range(p+1) for p in pows)):
        yield int_product(f**p for f,p in zip(factors,pp))


N,K = map(int,input().split())
A = list(map(int,input().split()))

def check(m):
    cost = 0
    S = sorted(a%m for a in A)
    total = sum(S)//m
    # print(m,S, total)
    return (sum(s for s in S[:N-total]) + sum(m-s for s in S[N-total:]))//2

for d in sorted(divisors(sum(A)), reverse=True):
    # print(d,check(d))
    if check(d) <= K:
        print(d)
        break
