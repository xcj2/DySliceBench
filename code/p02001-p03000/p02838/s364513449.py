import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  k=[0]*60
  n=I()
  l=LI()

  for x in l:
    _a=bin(x)[2:]
    a=_a.zfill(60)

    for i,y in enumerate(a):
      if y=='1':
        k[59-i]+=1

  ans=0
  for i,x in enumerate(k):
    ans+=(n-x)*x*(2**i)
    ans%=mod

  return ans%mod

# main()
print(main())
