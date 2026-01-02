import sys
sys.setrecursionlimit(100000000)

N,M=map(int, input().split())
a = [0]*M
for i in range(M):
  a[i] = int(input())

def memoize(f):
  table = {}
  def func(*args):
    if not args in table:
      table[args] = f(*args)
    return table[args]
  return func

@memoize

def step(n):
  if n==0:
    return(1)
  elif n==1:
    return(1)
  else:
    return((step(n-1)+step(n-2))%1000000007)

if M==0:
  print(step(N))
else:
  b = [0]*(M+1)
  b[0] = step(a[0]-1)
  if M>=2:
    for i in range(M-1):
      if a[i+1]-a[i] == 1:
        b[i+1] = 0
      else:
        b[i+1] = step(a[i+1]-a[i]-2)
  b[M] = step(N-a[M-1]-1)

  answer = 1
  for i in range(M+1):
    answer = answer*b[i]%1000000007
  print(answer)