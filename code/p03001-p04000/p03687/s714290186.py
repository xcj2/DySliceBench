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
  s=S()

  a=list(set(s))

  ans=[]
  for x in a:
    c=0
    t=list(s)
    while True:
      if len(set(t))==1:
        break

      for i in range(len(t)-1):
        if t[i]==x or t[i+1]==x:
          t[i]=x
      t=t[:-1]

      c+=1

    ans.append(c)

  return min(ans)

print(main())
