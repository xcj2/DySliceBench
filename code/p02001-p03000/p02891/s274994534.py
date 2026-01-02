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

# Summarize count of factor within list
def summarize_list(l):
  sl=l

  a=sl[0]
  c=1
  res=[]

  for x in sl[1:]:
    if x==a:
      c+=1
    else:
      res.append([a,c])
      a=x
      c=1
  res.append([a,c])

  return res

def main():
  s=S()
  k=I()

  if len(s)==1:
    return k//2

  l=summarize_list(s)

  if len(l)==1:
    return (l[0][1]*k)//2

  ans=0
  bf=False
  
  if l[0][0]==l[-1][0] and (l[0][1]//2+l[-1][1]//2!=(l[0][1]+l[-1][1])//2):
    bf=True

  _ans=0
  for x in l:
    _ans+=x[1]//2
  ans+=_ans*k

  if bf:
    ans+=k-1

  return ans

# main()
print(main())
