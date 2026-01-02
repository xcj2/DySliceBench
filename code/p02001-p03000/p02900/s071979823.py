def gcd(a,b):
  while b!=0:a,b=b,a%b
  return a
def lcm(a,b):return a*b//gcd(a,b)

def ds(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  return divisors

import random
def is_prime(n):
  if n == 2: return True
  if n == 1 or n & 1 == 0: return False
  d = (n - 1) >> 1
  while d & 1 == 0:
    d >>= 1
  for k in range(100):
    a = random.randint(1, n - 1)
    t = d
    y = pow(a, t, n)
    while t != n - 1 and y != 1 and y != n - 1:
      y = (y * y) % n
      t <<= 1
    if y != n - 1 and t & 1 == 0: return False
  return True

A,B=map(int,input().split())
l=sorted(ds(gcd(A,B)))
n=0
for i in l:
  if is_prime(i)==True:n+=1
print(n+1)