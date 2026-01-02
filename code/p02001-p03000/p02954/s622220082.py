def count_section_by_zero(data):
  count = 0
  flg = False
  start = 0
  for i, d in enumerate(data):
    if flg is False and d != 0:
      count += 1
      flg = True
      
    if d == 0:
      flg = False
  return count

def input_list():
  return list(map(int, input().split()))

def input_list_str():
  return list(map(str, input().split()))

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# 2で割り切れる回数
def divide_two(arg):
  c = 0
  while True:
    if c >= 2:
      break
    if arg % 2 != 0:
      break
    arg //= 2
    c += 1
  return c

# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
  s = input()
  n = len(s)
  ans = [1]*n
  for i in range(0, n-2):
    if s[i] == "R" and s[i+1] == "R":
      ans[i+2] += ans[i]
      ans[i] = 0
  for i in range(n-1, -1, -1):
    if s[i] == "L" and s[i-1] == "L":
      ans[i-2] += ans[i]
      ans[i] = 0
  print(*ans)
  
import math
import fractions
import collections
import itertools
from functools import reduce
main()