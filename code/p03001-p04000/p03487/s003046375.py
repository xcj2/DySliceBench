import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  N=int(input())
  l=LI()

  l.sort()
  l.append(inf)

  c=0
  a=l[0]
  cnt=1
  for x in l[1:]:
    if a==x:
      cnt+=1
    else:
      if a<cnt:
        c+=cnt-a
      elif a==cnt:
        pass
      else:
        c+=cnt
      a=x
      cnt=1

  print(c)

main()
# print(main())
