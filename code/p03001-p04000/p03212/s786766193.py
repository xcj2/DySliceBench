import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# 10 -> n
def ten2n(a,n):
  x=a//n
  y=a%n
  if x:
    return ten2n(x,n)+str(y)
  return str(y)

def main():
  n=I()

  l=[]
  for i in range(pow(4,9)):
    l.append(ten2n(i,4).replace('3','7').replace('2','5').replace('1','3'))

  cnt=0
  for x in l:
    if int(x)<=n:
      if '3' in x and '5' in x and '7' in x and '0' not in x:
        cnt+=1
    else:
      break

  return cnt

print(main())
