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
  sl=sorted(l)

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
  s=list(S())
  t=summarize_list(s)

  if len(s)==1:
    return 'YES'
  if len(s)==2:
    if len(t)==2:
      return 'YES'
    return 'NO'
  if len(t)<=2:
    return 'NO'

  t=sorted(t,key=lambda x:x[1])
  # print(t)
  if t[2][1]-t[0][1]>=2:
    return 'NO'
  return 'YES'

# main()
print(main())
