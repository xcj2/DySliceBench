import math
from decimal import *
getcontext().prec = 50
a,b,c,d = map(int,input().split())

from functools import reduce
def gcd(a,b):
  if a < b:
    a, b = b, a
  while a % b != 0:
    a, b = b, a % b
  return b

def lcm_base(x, y):
  return (x * y) // gcd(x, y)

def lcm_list(numbers):
  return reduce(lcm_base, numbers, 1)

gcd = lcm_list([c,d])

def solve(n):
	start = n * math.ceil(Decimal(a) / Decimal(n))
	end = n * (Decimal(b) // Decimal(n))
	#print(start,end)
	return (end - start) // n + 1

#print(solve(c),solve(d),solve(gcd))
ans = solve(c) + solve(d) - solve(gcd)
#print(ans)
print(b - a - ans + 1)
