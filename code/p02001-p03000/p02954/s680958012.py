import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  s=S()
  l=[1]*len(s)

  ans=[0]*len(s)

  c1=c2=0
  f=inf
  for i in range(len(s)-1):
    # print(ans)
    if s[i]=='R':
      if c1!=0 and c2!=0:
        if (max(c1,c2)-1)%2==1:
          if c1>=c2:
            ans[f+1]=-(-(c1+c2)//2)
            ans[f]=(c1+c2)//2
          else:
            ans[f]=-(-(c1+c2)//2)
            ans[f+1]=(c1+c2)//2
        else:
          if c1>=c2:
            ans[f]=-(-(c1+c2)//2)
            ans[f+1]=(c1+c2)//2
          else:
            ans[f+1]=-(-(c1+c2)//2)
            ans[f]=(c1+c2)//2
        f=inf
        c1=0
        c2=0
      c1+=1

      if s[i+1]=='R':
        ans[i]=0
      else:
        # ここはOK
        f=i
    else:
      c2+=1
      if s[i-1]=='L':
        ans[i]=0

  # print(c1,c2)
  c2+=1
  # if s[-2]=='L':
  # if (max(c1,c2)-1)%2==1:
  #   ans[f+1]=-(-(c1+c2)//2)
  #   ans[f]=(c1+c2)//2
  # else:
  #   ans[f]=-(-(c1+c2)//2)
  #   ans[f+1]=(c1+c2)//2
    
  if (max(c1,c2)-1)%2==1:
    if c1>=c2:
      ans[f+1]=-(-(c1+c2)//2)
      ans[f]=(c1+c2)//2
    else:
      ans[f]=-(-(c1+c2)//2)
      ans[f+1]=(c1+c2)//2
  else:
    if c1>=c2:
      ans[f]=-(-(c1+c2)//2)
      ans[f+1]=(c1+c2)//2
    else:
      ans[f+1]=-(-(c1+c2)//2)
      ans[f]=(c1+c2)//2

  # else:
    # print(c1,c2,f)

  return ' '.join([str(x) for x in ans])

# main()
print(main())
