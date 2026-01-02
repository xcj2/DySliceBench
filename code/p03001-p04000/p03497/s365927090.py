def main():
  n, k = input_list()
  a = list(input_list())
  kind = len(set(a[:]))
  if kind <= k:
    print(0)
    exit()
  need = kind - k
  ac = collections.Counter(list(a))
  ans = 0
  for v in sorted(ac.items(), key=lambda x: x[1]):
    if need == 0:
      break
    ans += v[1]
    need -= 1
  print(ans)
  
def input_list():
  return map(int, input().split())

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