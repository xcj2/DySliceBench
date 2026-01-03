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
  h,w=LI()

  if h%3==0 or w%3==0:
    return 0

  ans=inf
  for i in range(1,h):
    a=i*w
    b=(h-i)*(w//2)
    c=(h-i)*(-(-w//2))
    ans=min(ans,max([a,b,c])-min([a,b,c]))

    a=i*w
    b=(h-i)//2*w
    c=-(-(h-i)//2)*w
    ans=min(ans,max([a,b,c])-min([a,b,c]))

  for i in range(1,w):
    a=i*h
    b=(w-i)*(h//2)
    c=(w-i)*(-(-h//2))
    ans=min(ans,max([a,b,c])-min([a,b,c]))

    a=i*h
    b=(w-i)//2*h
    c=-(-(w-i)//2)*h
    ans=min(ans,max([a,b,c])-min([a,b,c]))

  return ans

# main()
print(main())
