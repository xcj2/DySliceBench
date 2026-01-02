import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

visited=[False]*(10**5)
ans=[-1]*(10**5)

def f(n,edges,s):
  all_visited=True
  for i in range(n):
    if visited[i]==False:
      all_visited=False
      break
  if all_visited:
    return

  for x,c in edges[s]:
    if visited[x]:
      continue
    if ans[s]==0:
      if c%2==1:
        ans[x]=1
      else:
        ans[x]=0
    else:
      if c%2==1:
        ans[x]=0
      else:
        ans[x]=1
    visited[x]=True
    f(n,edges,x)

def main():
  n=I()

  edges=[[] for _ in range(n)]
  for _ in range(n-1):
    a,b,c=LI()
    a-=1
    b-=1
    edges[a].append([b,c])
    edges[b].append([a,c])

  ans[0]=0
  visited[0]=True

  f(n,edges,0)

  for x in ans[:n]:
    print(x)

main()
# print(main())
