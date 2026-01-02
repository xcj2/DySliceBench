def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y) 

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def isPrime(n):
  if n <= 2:
    return True
  m = int((n**0.5)//1 + 1)
  for p in range(2, m):
      if n % p == 0:
        return False
  return True
    
a,b = map(int,input().split())
gcd = gcd(a,b)
yks = make_divisors(gcd)
ans = 0
for i in yks:
  if isPrime(i):
    ans +=1
print(ans)