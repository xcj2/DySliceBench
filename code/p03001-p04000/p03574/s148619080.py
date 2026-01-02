import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  h,w=LI()

  a=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

  l=[]
  for i in range(h):
    l.append(list(S()))

  for i in range(h):
    for j in range(w):
      if l[i][j]=='#':
        continue
      c=0
      for x in a:
        p=i+x[0]
        q=j+x[1]
        if 0<=p and p<h and 0<=q and q<w:
          if l[p][q]=='#':
            c+=1
      l[i][j]=str(c)

  for x in l:
    print(''.join(x))

main()
