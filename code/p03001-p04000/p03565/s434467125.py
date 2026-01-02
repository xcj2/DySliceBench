import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  s=S()
  t=S()

  for i in range(len(s)-len(t)+1)[::-1]:
    x=s[i:i+len(t)]
    f=True
    for j in range(len(t)):
      if t[j]!=x[j] and x[j]!='?':
        f=False

    if f:
      return s[:i].replace('?','a')+t+s[i+len(t):].replace('?','a')

  return 'UNRESTORABLE'

print(main())
