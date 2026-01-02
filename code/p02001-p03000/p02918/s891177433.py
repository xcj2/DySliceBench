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
def summarize_list(sl):

  a=sl[0]
  c=1
  res=[]

  for x in sl[1:]:
    if x==a:
      c+=1
    else:
      res.append(c)
      a=x
      c=1
  res.append(c)

  return res
# Summarize count of factor within list --- END ---

def main():
  n,k=LI()
  s=list(S())

  s=summarize_list(s)

  if 2*k+1>=len(s):
    return n-1

  s=[0]+s

  for i in range(len(s)-1):
    s[i+1]+=s[i]
  # print(s)

  l1=[0]*len(s)
  l2=[0]*len(s)

  for i in range(1,len(s)):
    l1[i]+=l1[i-1]
    l1[i]+=s[i]-s[i-1]-1

  for i in range(1,len(s))[::-1]: 
    l2[i-1]+=l2[i]
    l2[i-1]+=s[i]-s[i-1]-1

  # print(s)
  # print(l1)
  # print(l2)

  ans=-inf
  for i in range(len(s)-(2*k+1)):
    a=s[2*k+1+i]
    b=s[i]
    # print(a,b)
    c=l1[i]
    d=l2[2*k+1+i]
    ans=max(ans,a-b+c+d)

  return ans-1

# main()
print(main())
