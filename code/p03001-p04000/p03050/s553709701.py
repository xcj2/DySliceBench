import sys
import random
import itertools
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n = int(input())

import math
def factorization(n):
    def factor_sub(n, m):
        c = 0
        while n % m == 0:
            c += 1
            n //= m
        return c, n
    #
    buff = []
    c, m = factor_sub(n, 2)
    if c > 0: buff.append((2, c))
    c, m = factor_sub(m, 3)
    if c > 0: buff.append((3, c))
    x = 5
    while m >= x * x:
        c, m = factor_sub(m, x)
        if c > 0: buff.append((x, c))
        if x % 6 == 5:
            x += 2
        else:
            x += 4
    if m > 1: buff.append((m, 1))
    return buff
#a = factorization(n)
#b = []
#for i,j in a:
#  b.append(i)
def divisor_sub(p, q):
    a = []
    for i in range(0, q + 1):
        a.append(p ** i)
    return a

def divisor(n):
    if n == 1:
      return([1])
    xs = factorization(n)
    ys = divisor_sub(xs[0][0], xs[0][1])
    for p, q in xs[1:]:
        ys = [x * y for x in divisor_sub(p, q) for y in ys]
    return sorted(ys)
#素因数列挙
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  table = set(table)
  table = list(table)
  return table

a = divisor(n)
ans = []
a.remove(n)
for i in a:
    b = (n-i)//i
    if n//b == n %b:
        ans.append(b)
print(sum(ans))