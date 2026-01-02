import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=1000000007
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

  l=summarize_list(s)
  # print(l)

  # 1 0 1 0... の形にする
  if s[0]=='0':
    l=[0]+l

  # ...0 1 0 1 の形にする
  if s[-1]=='0':
    l+=[0]

  # 累積和
  for i in range(len(l)-1):
    l[i+1]+=l[i]

  l=[0]+l

  # print(l)

  ans=0
  left=0
  while True:
    right=min(len(l)-1,left+2*k+1)
    if left>=len(l):
      return ans

    # print(right,left)
    ans=max(ans,l[right]-l[left])

    left+=2

# main()
print(main())
