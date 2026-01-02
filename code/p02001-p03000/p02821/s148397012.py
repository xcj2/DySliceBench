N, M = map(int, input().split())
A = sorted(list(map(int,input().split())), reverse=True)

# jとの組み合わせがx以上になるiの個数
def combinations(x):
  s = 0
  i = 0
  for j in reversed(range(N)):
    while i<N and A[i]+A[j]>=x:
      i += 1
    s += i
  return s
 
#↑のような組み合わせの合計幸福度
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
 
#
def bsearch(l, u):
  m = (l+u)//2
  c = combinations(m)
#   print(f"m{m}, c{c},c-M{c-M}")
  if c<M:
    return bsearch(l, m)
  else:
    if l==m:
      return (l, c-M)
    return bsearch(m, u)
 
x, dm = bsearch(0, A[0]*2+1)
print(koufukudo(x)-dm*x)