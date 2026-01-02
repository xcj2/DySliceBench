import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  ml=[]
  al=[]
  rl=[]
  cl=[]
  hl=[]

  n=I()
  for _ in range(n):
    s=S()
    if s[0]=='M':
      ml.append(s)
    elif s[0]=='A':
      al.append(s)
    elif s[0]=='R':
      rl.append(s)
    elif s[0]=='C':
      cl.append(s)
    elif s[0]=='H':
      hl.append(s)

  l=[len(ml),len(al),len(rl),len(cl),len(hl)]
  sm=0

  for i in range(2):
    for j in range(2):
      for k in range(2):
        for m in range(2):
          for n in range(2):
            lx=[i,j,k,m,n]
            if lx.count(1)==3:
              _s=1
              for x in range(len(lx)):
                if lx[x]==1:
                  _s*=l[x]
              sm+=_s

  return sm

print(main())
