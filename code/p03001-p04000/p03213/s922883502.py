from math import sqrt, ceil, factorial
def is_prime(num):
  for i in range(2, ceil(sqrt(num))+1):
    if num%i==0:
      return False
  return True

def permcnt(n, r):
  return factorial(n) // factorial(n-r)

def combcnt(n, r):
  return factorial(n) // (factorial(n-r)*factorial(r))

n = int(input())
pls = [2]
i=3
while i<=n:
  if is_prime(i):
    pls.append(i)
  i+=1

def factoring(num):
  return _factoring(num, dict())
  
def _factoring(num, p):
  for i in pls:
    if num % i == 0:
      if i in p:
        p[i] += 1
      else:
        p[i] = 1
      return _factoring(num//i, p)
  return p

factors = dict()
for i in range(1,n+1):
  for k, v in factoring(i).items():
    if k in factors:
      factors[k] += v
    else:
      factors[k] = v

cnt = 0

# 七五数がx^74の形となるケース
cnt += len(list(filter(lambda x:x[1]>=74, factors.items())))

# 七五数がx^2*y^24の形となるケース
xs = {k for k,v in factors.items() if 2<=v and v<24}
ys = {k for k,v in factors.items() if v>=24}
cnt += len(xs)*len(ys)
cnt += permcnt(len(ys), 2) if len(ys)>=2 else 0

# 七五数がx^4*y^14の形となるケース
xs = {k for k,v in factors.items() if 4<=v and v<14}
ys = {k for k,v in factors.items() if v>=14}
cnt += len(xs)*len(ys)
cnt += permcnt(len(ys), 2) if len(ys)>=2 else 0

# 七五数がx^2*y^5*z^5の形となるケース
xs = {k for k,v in factors.items() if 2<=v and v<4}
ys = {k for k,v in factors.items() if v>=4}
cnt += len(xs)*combcnt(len(ys),2) if len(ys)>=2 else 0
cnt += 3*combcnt(len(ys), 3) if len(ys)>=3 else 0

print(cnt)