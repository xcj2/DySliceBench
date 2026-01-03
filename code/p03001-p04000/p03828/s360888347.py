import math
N = int(input())
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
i = 2
primedic = {}
primelist = []#len = 168
while i <= 1000:
  if is_prime(i) == True:
    primedic[i] = 0
    primelist.append(i)
  i += 1
def usage(n):
    fct = factorize(n)
    return(fct)
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct
def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a
j = 2
while j <= N:
  li = usage(j)
  for array in li:
    primedic[array[0]] += array[1]
  j += 1
ans = 1
for keys in primedic:
  ans = (ans*(primedic[keys]+1))%(10**9+7)
print(ans)