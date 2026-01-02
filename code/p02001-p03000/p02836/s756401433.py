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
  s=list(S())

  a=s[:len(s)//2]
  if len(s)%2==0:
    b=s[len(s)//2:]
  else:
    b=s[len(s)//2+1:]

  # print(a)
  # print(b)

  ans=0
  a.reverse()

  for i in range(len(s)//2):
    x=a[i]
    y=b[i]

    if x!=y:
      ans+=1

  return ans

# main()
print(main())
