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
  l=[]

  for i in range(n):
    l.append([i,I()])

  l2=copy.deepcopy(l)

  l2=sorted(l2,key=lambda x:x[1])

  ans=0
  for i,x in enumerate(l2):
    if i%2!=x[0]%2:
      ans+=1
  return ans//2

# main()
print(main())
