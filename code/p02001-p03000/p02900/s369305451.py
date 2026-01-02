def md(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def gcd(a,b):
  while b != 0:
    a, b = b, a%b
  return a

def isp(n):
  if n < 4:
    return True
  else:
    for i in range(2, int(n**0.5)+1):
      if n % i == 0:
        return False
    return True
    
A, B = map(int, input().split())
N = gcd(max(A, B), min(A, B))
D = md(N)

ans = 0

for d in D:
  if isp(d):
    ans += 1
    
print(ans)