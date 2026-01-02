import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Factoring by trial split -- START --
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
# Factoring by trial split --- END ---

# Summarize count of factor within list -- START --
def summarizeList(l):
  sl=sorted(l)

  a=sl[0]
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
# Summarize count of factor within list --- END ---

def main():
  n=I()
  ans=0

  for k in range(1,n+1):
    ans+=int((k/2)*(n//k)*(1+n//k))

  # for i in range(1,n+1):
  #   x=1
  #   if i==1:
  #     pass
  #   else:
  #     pl=getPrimeList(i)
  #     pl=summarizeList(pl)
  #     for a,c in pl:
  #       x*=(c+1)

  #   ans+=i*x

  return ans

# main()
print(main())
