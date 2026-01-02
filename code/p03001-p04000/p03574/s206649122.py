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
      if l[i][j]!='#':
        c=0
        for x in a:
          if i+x[0]>=0 and i+x[0]<h and j+x[1]>=0 and j+x[1]<w:
            if l[i+x[0]][j+x[1]]=='#':
              c+=1

          l[i][j]=str(c)

  for x in l:
    print(''.join(x))

main()
