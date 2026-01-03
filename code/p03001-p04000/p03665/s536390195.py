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
  n,p=LI()
  l=LI()

  la=[]
  lb=[]

  for x in l:
    if x%2==1:
      la.append(x)
    else:
      lb.append(x)

  # lbから偶数個選ぶ方法は何通り？
  bc=0
  for i in range(len(lb)+1):
    bc+=nCr(len(lb),i)
    # print(bc)

  ans=0
  for i in range(len(la)+1):
    if p==0:
      r=i*2
    else:
      r=i*2+1

    ans+=nCr(len(la),r)*bc

  return ans

print(main())
