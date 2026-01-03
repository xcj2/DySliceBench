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

  l=['dream','dreamer','erase','eraser']

  while True:
    a=s[-5:]
    b=s[-7:]
    c=s[-6:]

    if a==l[0]:
      s=s[:-5]
    elif b==l[1]:
      s=s[:-7]
    elif a==l[2]:
      s=s[:-5]
    elif c==l[3]:
      s=s[:-6]
    else:
      if s=='':
        return 'YES'
      else:
        return 'NO'

print(main())
