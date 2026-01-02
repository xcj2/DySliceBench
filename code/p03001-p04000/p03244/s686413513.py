def main():
  n = int(input())
  v = input_list()
  evens = []
  odds = []
  vs = v[:]
  kind = len(set(vs))
  if kind == 1:
    print(n//2)
    exit(0)
  
  for i, vv in enumerate(v):
    if i % 2 == 0:
      evens.append(vv)
    else:
      odds.append(vv)
  ec = collections.Counter(evens)
  oc = collections.Counter(odds)
  m = n//2
  
  ans = 0
  em = ec.most_common()
  om = oc.most_common()
  if em[0][0] == om[0][0]:
    p1 = m-em[0][1] + m-om[1][1]
    p2 = m-em[1][1] + m-om[0][1]
    print(min(p1,p2))
  else:
    print(m-em[0][1] + m-om[0][1])
  
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

import math
import fractions
import collections
from functools import reduce
main()