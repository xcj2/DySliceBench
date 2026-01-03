import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# 方針
# 1個のやつは何もしないでOK
# 合計個数が奇数の数字は自己解決する（最終的に1になる）
# 偶数になる数字は組を作ると解決する（2,2,5,5 のような場合）
# 偶数になる数字の組から漏れた数字は削られる

def main():
  n=I()
  l=LI()

  l.sort()

  l2=[]

  a=l[0]
  c=1
  ans=0
  aa=0
  for x in l[1:]:
    if x==a:
      c+=1
    else:
      if c==1:
        ans+=1
      else:
        if c%2==0:
          aa+=1
        else:
          ans+=1
      a=x
      c=1
  if c==1:
    ans+=1
  else:
    if c%2==0:
      aa+=1
    else:
      ans+=1

  return ans+aa-aa%2

print(main())
