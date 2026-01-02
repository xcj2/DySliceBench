import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Summarize count of factor within list -- START --
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
# Summarize count of factor within list --- END ---

# nCr -- START --
def nCr(n):
  return (n*(n-1))//2
# nCr --- END ---

def main():
  n=I()
  l=LI()
  mp=[0]*(n+1)

  sl=summarize_list(l)
  # print(sl)

  ans=0
  for x,c in sl:
    mp[x]=c
    ans+=nCr(c)

  # print(mp)
  # print(ans)

  for x in l:
    print(ans-nCr(mp[x])+nCr(mp[x]-1))

main()
# print(main())
