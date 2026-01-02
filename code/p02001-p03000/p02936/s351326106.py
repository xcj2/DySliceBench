import math,itertools,fractions,heapq,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

nmax=2*10**5+10
graph=[[] for _ in range(nmax)]
level=[-1]*nmax

def dfs(n,s,l):
  if len(graph[s])==0:
    return
  for e in graph[s]:
    if level[e]==-1:
      level[e]=level[s]+1
    if level[e]>level[s]:
      l[e]+=l[s]
      dfs(n,e,l)

def main():
  n,q=LI()
  for _ in range(n-1):
    a,b=LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
  l=[0]*n
  for _ in range(q):
    a,b=LI()
    l[a-1]+=b

  level[0]=0
  dfs(n,0,l)

  return ' '.join([str(x) for x in l])

# main()
print(main())
