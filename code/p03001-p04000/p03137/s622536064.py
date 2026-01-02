def chunk_list(index_list, data):
  result = []
  start = 0
  for i in index_list:
    result.append(data[start:i+1])
    start = i+2
    print(start)
  result.append(data[start:len(data)])
  return result
  
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
  return map(str, input().split())

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

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

import math
import fractions
import collections
from functools import reduce

def main():
  n, m = input_list()
  if n >= m:
    print(0)
    exit(0)
  x = list(set(input_list()))
  sx = list(sorted(x))
  diffs = []
  for i, xv in enumerate(range(len(x)-1)):
    diff = abs(sx[i+1]-sx[i])
    diffs.append(diff)
  sd = list(sorted(diffs, reverse=True))

  for i in range(n-1):
    sd[i] = 0
    if i == m-1:
      break

  ans = 0
  for a in sd:
    ans += a
  print(ans)
main()