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

dp=[-1]*100100
G=[[] for _ in range(100100)]

def dfs(v):
  if dp[v]!=-1:
    return dp[v]
  dp[v]=r=max(dfs(w) for w in G[v])+ 1 if G[v] else 0
  return r

def main():
  n,k=LI()

  for _ in range(k):
    a,b=LI()
    a-=1
    b-=1
    G[a].append(b)

  return max(dfs(v) for v in range(n))

# main()
print(main())
