def ints():
  return [int(x) for x in input().split()]
def ii():
  return int(input())

N, M = ints()
A = ints()
A.sort()
A.reverse()

def combinations(x):
  s = 0
  i = 0
  for j in reversed(range(N)):
    while i<N and A[i]+A[j]>=x:
      i += 1
    s += i
    
  return s

def koufukudo(x):
  s = 0
  si = 0
  i = 0
  for j in reversed(range(N)):
    while i<N and A[i]+A[j]>=x:
      si += A[i]
      i += 1
    s += si + A[j]*i
    
  return s


def bsearch(l, u):
  m = (l+u)//2
  c = combinations(m)
  if c<M:
    return bsearch(l, m)
  else:
    if l==m:
      return (l, c-M)
    return bsearch(m, u)

x, dm = bsearch(0, A[0]*2+1)
print(koufukudo(x)-dm*x)
