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
  l=LI()

  l=[0]+l+[0]
  n+=2

  sm=0
  for i in range(n-1):
    sm+=abs(l[i+1]-l[i])

  # print(sm)

  for i in range(1,n-1):
    _sm=sm
    _sm+=abs(l[i+1]-l[i-1])
    _sm-=abs(l[i]-l[i-1])
    _sm-=abs(l[i+1]-l[i])
    print(_sm)

main()
# print(main())
