import sys,collections

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n=I()
  l=LI()

  # a1=(x1+x2)/2,a2=(x2+x3)/2,...,an=(xn+x1)/2
  # 2a1=x1+x2,2a2=x2+x3,...,2an=xn+x1
  # x1=S-(x2+x3+...+xn)
  # x1=S-2(a2+a4+...+an-1)
  # x2=2a1-x1
  # x3=2a2-x2
  # ...

  sm=sum(l)
  ans=[]
  tmp=0
  for i,x in enumerate(l):
    if i%2==1:
      tmp+=x
  x1=sm-2*tmp
  ans.append(x1)

  for ai in l[:-1]:
    xp=2*ai-x1
    ans.append(xp)
    x1=xp

  return ' '.join([str(x) for x in ans])

# main()
print(main())
