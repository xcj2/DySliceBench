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

def main():
  n=I()
  G=[[]*n for _ in range(n)]
  vp=[]

  for _ in range(n-1):
    a,b=LI()
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
    vp.append((a,b))

  k=0
  d={}
  cs=[0]*n

  used=[False]*n
  used[0]=True
  q=collections.deque()
  q.append(0)
  while q:
    v=q.popleft()
    k=max(k,len(G[v]))
    cur=1
    for u in G[v]:
      if used[u]:
        continue
      if cur==cs[v]:
        cur+=1
      cs[u]=d[(u,v)]=d[(v,u)]=cur
      cur+=1
      used[u]=True
      q.append(u)

  print(k)
  for a,b in vp:
    print(d[(a,b)])

main()
# print(main())
