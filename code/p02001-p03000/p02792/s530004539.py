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

  l=[[0 for _ in range(10)]for __ in range(10)]

  for i in range(1,n+1):
    a=str(i)[0]
    b=str(i)[-1]

    l[int(a)][int(b)]+=1

  ans=0
  for i in range(10):
    for j in range(10):
      ans+=l[i][j]*l[j][i]

  return ans

# main()
print(main())
