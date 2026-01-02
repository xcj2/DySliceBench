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
  n=I()
  s=S()

  r=[0]*(n+1)
  g=[0]*(n+1)
  b=[0]*(n+1)

  for i,x in enumerate(s):
    if x=='R':
      r[i+1]+=1
    elif x=='G':
      g[i+1]+=1
    else:
      b[i+1]+=1
    r[i+1]+=r[i]
    g[i+1]+=g[i]
    b[i+1]+=b[i]

  # print(r)
  # print(g)
  # print(b)

  ans=0
  for i,x in enumerate(s):
    for j in range(i+1,n):
      y=s[j]

      k=j+(j-i)
      if k<n:
        # print(x,y,i,j,k,s[k])
        if x=='R' and y=='G':
          ans+=b[k]-b[j]+b[n]-b[k]
        elif x=='R' and y=='B':
          ans+=g[k]-g[j]+g[n]-g[k]
        elif x=='G' and y=='B':
          ans+=r[k]-r[j]+r[n]-r[k]
        elif x=='G' and y=='R':
          ans+=b[k]-b[j]+b[n]-b[k]
        elif x=='B' and y=='R':
          ans+=g[k]-g[j]+g[n]-g[k]
        elif x=='B' and y=='G':
          ans+=r[k]-r[j]+r[n]-r[k]
        
        z=s[k]
        if j-i==k-j and len(set([x,y,z]))==3:
          ans-=1

      else:
        if x=='R' and y=='G':
          ans+=b[n]-b[j]
        elif x=='R' and y=='B':
          ans+=g[n]-g[j]
        elif x=='G' and y=='B':
          ans+=r[n]-r[j]
        elif x=='G' and y=='R':
          ans+=b[n]-b[j]
        elif x=='B' and y=='R':
          ans+=g[n]-g[j]
        elif x=='B' and y=='G':
          ans+=r[n]-r[j]

  return ans

# main()
print(main())
