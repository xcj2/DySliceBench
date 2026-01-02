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
  n=I()
  l=LI()

  l2=copy.deepcopy(l)
  l2.sort()

  c=0
  l3=[]
  l4=[]
  for i in range(n):
    if l[i]!=l2[i]:
      c+=1
      l3.append(l[i])
      l4.append(l2[i])

  if c==0:
    return 'YES'
  l3.sort()
  l4.sort()
  if c==2 and l3==l4:
    return 'YES'
  return 'NO'

# main()
print(main())
