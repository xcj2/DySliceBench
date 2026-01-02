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

  if len(s)>9:
    return 'NO'
  if len(s)==9:
    if s=='AKIHABARA':
      return 'YES'
    return 'NO'
  if len(s)==8:
    if s=='KIHABARA' or s=='AKIHBARA' or s=='AKIHABRA' or s=='AKIHABAR':
      return 'YES'
    return 'NO'
  if len(s)==7:
    if s=='KIHBARA' or s=='KIHABRA' or s=='KIHABAR' or s=='AKIHBRA' or s=='AKIHBAR' or s=='AKIHABR':
      return 'YES'
    return 'NO'
  if len(s)==6:
    if s=='KIHBRA' or s=='KIHABR' or s=='KIHBAR' or s=='AKIHBR':
      return 'YES'
    return 'NO'
  if len(s)==5:
    if s=='KIHBR':
      return 'YES'
    return 'NO'
  else:
    return 'NO'

# main()
print(main())
