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

  l2=[400,800,1200,1600,2000,2400,2800,3200]
  l3=[0]*9

  for x in l:
    l3[bisect.bisect_right(l2,x)]+=1

  # print(l3)

  sm=0
  for x in l3[:-1]:
    if x!=0:
      sm+=1

  if sm==0:
    print(1,l3[-1])
  else:
    print(sm,sm+l3[-1])

main()
