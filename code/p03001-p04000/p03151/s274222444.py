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
  n=I()
  l1=LI()
  l2=LI()

  sm1=sum(l1)
  sm2=sum(l2)

  if sm1<sm2:
    return -1

  a=[]
  b=[]
  for i,x in enumerate(l1):
    y=l2[i]
    if x<y:
      a.append(y-x)
    elif x>y:
      b.append(x-y)
  b.sort()

  if len(a)==0:
    return 0

  # print(a)
  # print(b)

  ans=len(a)
  _lenb=len(b)
  _a=a.pop()
  _b=b.pop()
  while True:
    if _b>=_a:
      _b-=_a
      if len(a)<=0:
        break
      else:
        _a=a.pop()

    else:
      _a-=_b
      _b=b.pop()

  return ans+_lenb-len(b)

# main()
print(main())
