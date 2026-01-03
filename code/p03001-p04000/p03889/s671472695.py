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
  s=S()
  t=s
  s=list(s)
  s.reverse()
  s=''.join(s)
  s=s.replace('b','1')
  s=s.replace('d','2')
  s=s.replace('p','3')
  s=s.replace('q','4')
  s=s.replace('1','d')
  s=s.replace('2','b')
  s=s.replace('3','q')
  s=s.replace('4','p')
  if s==t:
    return 'Yes'
  return 'No'

# main()
print(main())
