import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  s=list(S())

  l=[['d', 'r', 'e', 'a', 'm'],
  ['d', 'r', 'e', 'a', 'm', 'e', 'r'],
  ['e', 'r', 'a', 's', 'e'],
  ['e', 'r', 'a', 's', 'e', 'r']]

  while True:
    if len(s)<=4:
      break
    else:
      if l[0]==s[-5:]:
        [s.pop() for _ in ' '*5]
      elif l[1]==s[-7:]:
        [s.pop() for _ in ' '*7]
      elif l[2]==s[-5:]:
        [s.pop() for _ in ' '*5]
      elif l[3]==s[-6:]:
        [s.pop() for _ in ' '*6]
      else:
        return 'NO'

  if len(s)==0:
    return 'YES'
  return 'NO'

print(main())
