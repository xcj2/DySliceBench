def count_baisuu(a, b):
  return b - (a % b)
  
def main():
  n = int(input())
  alist = []
  blist = []
  ab = []
  for i in range(n):
    a, b = input_list()
    ab.append((a, b))
    alist.append(a)
    blist.append(b)
  
  s = 0
  res = 0
  for i in range(n-1, -1, -1):
    alist[i] += res
    
    if alist[i] % blist[i] == 0:
      continue
    res += blist[i] - (alist[i]%blist[i])
  print(res)
  exit()
  dp = [0]*n
  i = n - 1
  res = 0
  for a, b in reversed(ab):
    if i != n-1:
      res += dp[i]
    a += res
    if a % b == 0:
      continue
    if a < b:
      dp[i] = b - a
    else:
      dp[i] = count_baisuu(a, b)
    i -= 1
  print(dp)
  
  

import math
import fractions
from functools import reduce


def input_list():
  return map(int, input().split())

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
main()