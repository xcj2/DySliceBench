import math

def func(b,n):
  if b > n:
    return n
  else:
    return func(b, math.floor(n/b)) + (n % b)

def _func(b,n):
  x = n
  ret = 0
  while True:
    if b > x:
      return ret + x
    else:
      ret += x % b
      x = math.floor(x/b)

def solve(n,s):
  if n == s:
    return n+1
  ans = float('inf')
  for b in range(2,math.floor(math.sqrt(n))+1):
    if _func(b,n) == s:
      return b

  for p in range(1,math.floor(math.sqrt(n))+1):
    if (n-s) % p == 0:
      b = int((n-s)/p)+1
      if b < 2:
        continue
      if _func(b, n) == s:
        ans = min(ans, b)

  if ans < float('inf'):
    return ans
  else:
    return -1

if __name__  == "__main__":
  n = int(input())
  s = int(input())
  ans = solve(n,s)
  print(ans)
