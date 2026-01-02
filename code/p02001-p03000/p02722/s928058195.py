n = int(input())
def make_divisors(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      x = n//i
      while x%i == 0:
        x = x//i
      if x%i == 1:
        ans += 1
  return
def count_divisors(n):
  c = 0
  for i in range(1, int(n**0.5)):
    if n % i == 0:
      c += 2
  if n%int(n**0.5) == 0:
    if n==n//int(n**0.5):
      c += 1
    else:
      c += 2
  return c
ans = 0
def count_divisors(n):
  c = 0
  for i in range(1, int(n**0.5)):
    if n % i == 0:
      c += 2
  if n%int(n**0.5) == 0:
    if int(n**0.5)==n//int(n**0.5):
      c += 1
    else:
      c += 2
  return c
ans += count_divisors(n-1)
def make_divisors(n):
  c = 0
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      x = n//i
      while x%i == 0:
        x = x//i
      if x%i == 1:
        c += 1
  return c
ans += make_divisors(n)
print(ans)




