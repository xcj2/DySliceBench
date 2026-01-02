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

def main():
  n,m=LI()

  l=[]
  for _ in range(m):
    a=LI()
    l.append(a[1:])

  l2=LI()

  pattern=[]
  for i in range(1<<n):
    _l=[]
    for j in range(n):
      _l.append(1 if i&(1<<j) else 0)
    pattern.append(_l)

  ans=0
  for x in pattern:
    f=True
    for i,y in enumerate(l):
      on_num=0
      for z in y:
        on_num+=x[z-1]

      if not f:
        break
      if f and l2[i]!=on_num%2:
        f=False
        break

    if f:
      ans+=1

  return ans

# main()
print(main())
