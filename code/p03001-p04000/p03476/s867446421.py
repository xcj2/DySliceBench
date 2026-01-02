#!/opt/local/bin/python3

# AtCoder Beginner Contest 084
# D: 2017-like Number

import sys, math
from itertools import accumulate

MAX_N = 100000

def sieve():
  isprime = [i >= 2 for i in range(MAX_N + 1)]
  for p in range(2, MAX_N + 1):
    if isprime[p]:
      for q in range(p + p, MAX_N + 1, p):
        isprime[q] = False
  return isprime

def isPrime(n):
  isPrime._ = isPrime._ or sieve()
  return isPrime._[n]
isPrime._ = None

def is2017like(n):
  return isPrime(n) and isPrime((n + 1) // 2)

# the number of 2017-like numbers less than or equal to n.
def n2017likeUnder(n):
  if n2017likeUnder._ == None:
    lis = [1 if is2017like(i) else 0 for i in range(MAX_N + 1)]
    n2017likeUnder._ = list(accumulate(lis))
  return n2017likeUnder._[n]
n2017likeUnder._ = None

# the number of 2017-like numbers between l and r.
def solve(l, r):
  return n2017likeUnder(r) - n2017likeUnder(l - 1)

Q = int(sys.stdin.readline())
for i in range(Q):
  l, r = [int(w) for w in sys.stdin.readline().split()]
  print(solve(l, r))
