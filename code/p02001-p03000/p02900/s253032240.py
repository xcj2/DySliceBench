import math

a, b = map(int, input().split())

def gcd(x, y):
  z = x % y
  if z == 0:
    return y
  else:
    return gcd(y, z)
  
def common_divisors(x, y):
  xd = make_divisors(x)
  xd.append(1)
  xd.append(x)
  yd = make_divisors(y)
  yd.append(1)
  yd.append(y)
  return set(xd).intersection(yd)

def make_divisors(n):
  divisors = [] 
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)
  return divisors

divisors = common_divisors(a, b)
divisors_set = frozenset(divisors)

res = []

for n in divisors:
  if n == 1 or n == 2 or n == 3:
    res.append(n)
  elif n % 2 == 0:
    continue
  else:
    dvs = set(make_divisors(n))
    if len(dvs) == 0 or not dvs <= divisors_set:
      res.append(n)

print("{}".format(len(res)))