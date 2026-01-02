import math

def hcfnaive(a, b):
    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)

def gcd(a, b, c):
    return hcfnaive(a, hcfnaive(b, c))

##def gcd(a, b, c, cnt):
  ##  i = 0
    ####  i = i + 1
        ##if len(list(filter(is_prime, [a, b, c]))) == 0:
          ##  if (a % i == 0) and(b % i == 0) and (c % i == 0):
            ##    return gcd(a / i, b / i, c / i, cnt * i)
        ##else:
          ##  return cnt

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

ans = 0
k = int(input())
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans = ans + gcd(a, b, c)

print(ans)