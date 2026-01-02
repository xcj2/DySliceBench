def ints():
  return [int(x) for x in input().split()]
def ii():
  return int(input())

N, M = ints()
A = ints()
A.sort()
A.reverse()

def combinations_and_kofukudo(x):
  c = 0
  k = 0
  si = 0
  i = 0
  for j in reversed(range(N)):
    while i<N and A[i]+A[j]>=x:
      si += A[i]
      i += 1
    c += i
    k += si + A[j]*i
    
  return (c, k)

def bsearch(l, u):
  m = (l+u)//2
  c, k = combinations_and_kofukudo(m)
  if c<M:
    return bsearch(l, m)
  else:
    if l==m:
      print(k-(c-M)*l)
      exit()
    return bsearch(m, u)

bsearch(0, A[0]*2+1)
