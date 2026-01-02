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
  a=[]
  for _ in range(h):
    a.append(S())

  row=[False]*h
  col=[False]*w

  for i in range(h):
    for j in range(w):
      if a[i][j]=='#':
        row[i]=True
        col[j]=True

  for i in range(h):
    if row[i]:
      for j in range(w):
        if col[j]:
          print(a[i][j], end='')
      print()

main()
