import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n=I()
  l=LI()

  l.sort()

  ans=[]
  # +オンリー
  if l[0]>=0:
    a=l[0]
    for i in range(1,n-1):
      b=l[i]
      ans.append([a,b])
      a-=b
    ans.append([l[-1],a])

    print(l[-1]-a)
    for x in ans:
      print(x[0],x[1])

  # +と-がある
  elif l[0]<0 and l[-1]>=0:
    a=l[0] #最低
    b=l[-1] #最高

    for x in l[1:-1]:
      if x<=0:
        ans.append([b,x])
        b-=x
      else:
        ans.append([a,x])
        a-=x
    ans.append([b,a])

    print(b-a)
    for x in ans:
      print(x[0],x[1])

  # -オンリー
  else:
    l.reverse()
    a=l[0]
    for i in range(1,n-1):
      b=l[i]
      ans.append([a,b])
      a-=b
    ans.append([a,l[-1]])

    print(a-l[-1])
    for x in ans:
      print(x[0],x[1])

main()
