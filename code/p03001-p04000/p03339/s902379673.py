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
  s=list(S())

  l1=[]
  l2=[]

  a=s[0]
  if a=='W':
    l1.append([1,0])
  else:
    l1.append([0,1])

  for i in range(1,len(s[1:])+1):
    if s[i]=='W':
      l1.append([l1[i-1][0]+1,l1[i-1][1]])
    else:
      l1.append([l1[i-1][0],l1[i-1][1]+1])

  _s=s[:]
  _s.reverse()

  a=_s[0]
  if a=='W':
    l2.append([1,0])
  else:
    l2.append([0,1])

  for i in range(1,len(_s[1:])+1):
    if _s[i]=='W':
      l2.append([l2[i-1][0]+1,l2[i-1][1]])
    else:
      l2.append([l2[i-1][0],l2[i-1][1]+1])

  l2.reverse()

  # print(l1)
  # print(l2)

  mn=inf
  for i in range(n):
    a=s[i]
    if a=='W':
      l1[i][0]-=1
      l2[i][0]-=1
    else:
      l1[i][1]-=1
      l2[i][1]-=1
    mn=min(mn,l1[i][0]+l2[i][1])

  return mn

print(main())
