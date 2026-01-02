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

  # c=0
  # while True:
  #   if s.count('ABC')>0:
  #     c+=s.count('ABC')
  #     s=s.replace('ABC','BCA')
  #   else:
  #     break

  # print(s)
  # return c

  s=list(s)
  s.reverse()
  s=''.join(s)

  cb_c=0
  sm=0
  f=False
  for i in range(len(s)):
    if f:
      f=False
      continue
    if s[i:i+2]=='CB':
      cb_c+=1
      f=True
    elif s[i]=='A':
      sm+=cb_c
    else:
      cb_c=0

  return sm

print(main())
