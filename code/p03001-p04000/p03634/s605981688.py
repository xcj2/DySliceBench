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

# dijkstra -- START --
def dijkstra(n,s,edge):
  d=[inf]*n
  used=[False]*n
  d[s]=0
  used[s]=True
  pq=[]
  for e in edge[s]:
    heapq.heappush(pq,e)
  while pq:
    c,v=heapq.heappop(pq)
    if used[v]:
      continue
    d[v]=c
    used[v]=True
    for nc,nv in edge[v]:
      if not used[nv]:
        nd=nc+c
        if d[nv]>nd:
          heapq.heappush(pq,(nd,nv))
  return d
# dijkstra --- END ---

def main():
  n=I()
  e=[[] for _ in range(n)]
  for _ in range(n-1):
    a,b,c=LI()
    a-=1
    b-=1
    e[a].append((c,b))
    e[b].append((c,a))

  q,k=LI()
  d=dijkstra(n,k-1,e)

  ans=[]
  for _ in range(q):
    x,y=LI()
    x-=1
    y-=1
    dist=d[x]+d[y]
    ans.append(dist)

  for x in ans:
    print(x)

main()
# print(main())
