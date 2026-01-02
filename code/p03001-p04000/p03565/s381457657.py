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
  t=S()

  for i in range(len(s)-len(t)+1)[::-1]:
    f=True
    for j in range(len(t)):
      # print(s[i+j],t[j])
      if s[i+j]!=t[j] and s[i+j]!='?':
        f=False
        break
    if f:
      return (s[:i]+t+s[i+len(t):]).replace('?','a')
  return 'UNRESTORABLE'

# main()
print(main())
