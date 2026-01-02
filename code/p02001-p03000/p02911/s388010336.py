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
  sl=sorted(l,reverse=True)

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
  n,k,q=LI()
  l=[I() for _ in range(q)]

  l=summarize_list(l)
  # print(l)

  for i in range(n):
    x=i+1

    if len(l)>0 and l[-1][0]==x:
      if l[-1][1]+k-q>0:
        print('Yes')
      else:
        print('No')
      l.pop()
    else:
      if k-q>0:
        print('Yes')
      else:
        print('No')

main()
# print(main())
