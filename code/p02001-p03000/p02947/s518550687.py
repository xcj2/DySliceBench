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

# nCr
def nCr(n,r):
  if n<r:
    return 0
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

def main():
  n=I()
  l=[]
  for i in range(n):
    a=list(S())
    a.sort()
    l.append(a)

  l.sort()

  a=l[0]
  c=1
  ans=0
  for x in l[1:]:
    if a==x:
      c+=1
    else:
      ans+=nCr(c,2)
      c=1
      a=x

  ans+=nCr(c,2)
  c=1
  a=x
  return ans

# main()
print(main())
