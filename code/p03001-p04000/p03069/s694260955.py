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
  ans=inf

  s=S()

  ans=min(ans,len(s)-s.count('.'))
  ans=min(ans,len(s)-s.count('#'))

  a=s.count('.')
  b=s.count('#')

  _a=0
  for i in range(n):
    if s[i]=='.':
      a-=1
    else:
      _a+=1
    ans=min(ans,_a+a)
    # print(ans)
  return ans

# main()
print(main())
