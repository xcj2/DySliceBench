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

def main():
  n,m=LI()
  ans=[-1]*n

  q=collections.deque()
  v=[[] for _ in range(n)]
  for _ in range(m):
    a,b=LI()
    a-=1
    b-=1
    v[a].append(b)
    v[b].append(a)
    if a==0:
      q.append((0,b,0))
    elif b==0:
      q.append((0,a,0))

  while q:
    moto,nxt,stp=q.popleft()
    if ans[nxt]==-1:
      ans[nxt]=moto
    else:
      continue

    for x in v[nxt]:
      if ans[x]==-1:
        q.append((nxt,x,stp+1))

  if -1 in ans[1:]:
    print('No')
    exit()

  print('Yes')
  for x in ans[1:]:
    print(x+1)

main()
# print(main())
