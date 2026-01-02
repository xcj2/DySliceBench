import math

def com(n, r):
  if r < 0 and r > n:
    return 0
  
  if r == 1:
    return n
  elif r == 2:
    return n * (n-1) / 2
  else:
    return n * (n-1) * (n-2) / 6

def pow(n, k):
  res = 1
  for i in range(k):
    res *= n

  return res

def solve(i, k, smaller):
  global P
  global N

  if i == P:
    if k == 0:
      return 1
    else:
      return 0

  if k == 0:
    return 1

  if smaller:
    return com(P-i, k) * pow(9, k)
  else:
    if (N[i] == '0'):
      return solve(i+1, k, False)
    else:      
      a = solve(i+1, k, True)
      b = solve(i+1, k-1, True) * (int(N[i]) - 1)
      c = solve(i+1, k-1, False)
      return a + b + c
    
N = input()
K = input()

P = len(N)

print(math.floor(solve(0, int(K), False)))