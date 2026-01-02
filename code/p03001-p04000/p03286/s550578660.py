N=int(input())
def f(x):
  #正の数xに対して-2進数表現の桁数を出力
  i=0
  counter=0
  while counter<x:
    counter+=2**i
    i+=2
  return i-1

def g(x):
  k=f(x)
  out=[1]
  for i in range(k-1, 1, -1):
    out.append(h(x, i))
  if x%2==0:
    out.append(0)
  else:
    out.append(1)
  return out

def h(x, i):
  j=i//2
  b=sum([2**(2*k) for k in range(j)])
  if ((x-b-1)//(2**(i-1)))%2==0:
    return 1
  else:
    return 0
  
def e(n):
  #nは負
  n_=-n
  i=1
  while n_>2**i:
    i+=2
    
  return 2**i+n

if N>0:
  out=g(N)
  out=map(str, out)
  out="".join(out)
elif N<0:
  N_=-N
  k=N_//2+N_%2
  out=g(k)
  out.append(N_%2)
  out=map(str, out)
  out="".join(out)
else:
  out=0
  
print(out)