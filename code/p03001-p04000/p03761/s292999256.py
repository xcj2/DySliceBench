import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  # a〜z
  l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  _l=[0]*26

  n=I()

  al=[]
  for _ in range(n):
    s=S()
    bl=_l[::]
    for x in s:
      bl[l.index(x)]+=1

    al.append(bl)

  s=''
  for i in range(len(l)):
    cnt=inf
    for j in range(len(al)):
      cnt=min(cnt,al[j][i])
    s+=l[i]*cnt

  return s

print(main())
