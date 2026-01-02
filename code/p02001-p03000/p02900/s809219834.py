a,b = map(int,input().split())

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table    

def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  for p in range(2, int(n**0.5)+1):
      if n % p == 0:
        return False
  return True

n = gcd(a,b)
lst = divisor(n)

ans = []
for x in lst:
    if isPrime(x):
        ans.append(x)
print(len(ans) + 1)