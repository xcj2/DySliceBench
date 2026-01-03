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

  l2=[]
  c=0
  for x in l:
    if x>=3200:
      c+=1
      l2.append(8)
    else:
      l2.append(x//400)

  l2=list(set(l2))

  if len(l2)!=1 and l2.count(8):
    l2.remove(8)

  if len(l2)==1 and l2[0]==8:
    c=max(0,c-1)

  print(len(l2),len(l2)+c)

main()
