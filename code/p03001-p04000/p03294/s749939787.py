import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Factoring by trial split
def getPrimeList(n):
  l=[]
  t=int(math.sqrt(n))+1
  
  for a in range(2,t):
    while n%a==0:
      n//=a
      l.append(a)
  
  if n!=1:
    l.append(n)
  
  return l

# Summarize count of factor within list
def summarize_list(l):
  sl=sorted(l)

  a=l[0]
  c=1
  res=[]

  for x in sl[1:]:
    if x==a:
      c+=1
    else:
      res.append([a,c])
      a=x
      c=1
  res.append([a,c])

  return res

def main():
  n=I()
  l1=LI()

  l2=[]
  for x in l1:
    _l=getPrimeList(x)
    l2+=summarize_list(_l)

  l2.sort(reverse=True)

  k=1
  a=l2[0]
  for x in l2[1:]:
    # print(x)

    if a[0]!=x[0]:
      k*=a[0]**a[1]
      a=x
      # print(k)

  k*=a[0]**a[1]
  k-=1

  # print(k)

  b=0
  for x in l1:
    b+=k%x

  return b

# main()
print(main())
