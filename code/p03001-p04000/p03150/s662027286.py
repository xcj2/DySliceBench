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

  if s[-7:]=='keyence':
    return 'YES'
  if s[:7]=='keyence':
    return 'YES'
  if s[0]=='k' and s[-6:]=='eyence':
    return 'YES'
  if s[:2]=='ke' and s[-5:]=='yence':
    return 'YES'
  if s[:3]=='key' and s[-4:]=='ence':
    return 'YES'
  if s[:4]=='keye' and s[-3:]=='nce':
    return 'YES'
  if s[:5]=='keyen' and s[-2:]=='ce':
    return 'YES'
  if s[:6]=='keyenc' and s[-1]=='e':
    return 'YES'
  return 'NO'

# main()
print(main())
