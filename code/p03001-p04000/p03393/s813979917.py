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

# a〜z
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def main():
  s=S()
  if s=='zyxwvutsrqponmlkjihgfedcba':
    return -1

  for x in s:
    if l.count(x)==0:
      return -1
    l.remove(x)

  if len(l)>0:
    return ''.join(s)+l[0]

  nakama=[]
  for i in range(len(s))[::-1]:
    nakama.sort()
    b=s[i]
    for a in nakama:
      if a>b:
        return s[:i]+a
    nakama.append(b)

# main()
print(main())
