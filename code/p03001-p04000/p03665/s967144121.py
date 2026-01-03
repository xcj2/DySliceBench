def main():
  n, p = input_list()
  a = list(input_list())
  # 全て偶数かどうか
  is_even = True
  for v in a:
    if v % 2 != 0:
      is_even = False
      break
  if is_even:
    if p == 0:
      print(2**n)
      exit()
    else:
      print(0)
      exit()
  else:
    print(2**(n-1))
  
  exit()
  if p == 0:
    # 偶数の場合：
    for i in range(n):
      if i % 2 == 0:
        r += combinations_count(n, i)
    if r % 2 != 0:
      r += 1
  else:
    # 奇数の場合：奇数を奇数個かける
    for i in range(n):
      if i % 2 != 0:
        r += combinations_count(n, i)
    if r > 0:
      r += 1
  print(r)  
  exit()
  for i in range(bi+1):
    fi = format(i, '0'+str(n)+'b')
    ans = 0
    for index, v in enumerate(fi):
      if v == '1':
        ans += a[index]
    if ans % 2 == p:
      r += 1
  print(r)
  
def input_list():
  return map(int, input().split())

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

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

import math
import fractions

from functools import reduce
main()