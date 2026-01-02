import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,m=LI()
  s=S()

  ans=[]
  counter=1
  for x in s[1:]:
    if x=='0':
      if counter>m:
        return -1
      ans.append(counter)
      counter=1
    else:
      counter+=1

  ans.reverse()
  _ans=[]

  sm=0
  for x in ans:
    if sm+x>m:
      _ans.append(sm)
      sm=x
    else:
      sm+=x
  if sm>0:
    _ans.append(sm)

  _ans.reverse()
  return ' '.join([str(x) for x in _ans])


# main()
print(main())
