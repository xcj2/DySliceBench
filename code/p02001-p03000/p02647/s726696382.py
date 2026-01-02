import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,k=LI()
  l=LI()

  for i in range(k):
    nxtl=[0]*n

    # 実験 n=100 k=100 l=[0]*100 で回すとi=13で全部行き渡るようになった
    # f=False
    # for a in range(n):
    #   if l[a]<n-1:
    #     f=True
    # if not f:
    #   return i

    ff=True
    for j in range(n):
      left=j-l[j]
      if left<0:
        left=0
      else:
        ff=False
      nxtl[left]+=1

      right=j+l[j]+1
      if right<n:
        nxtl[right]-=1
        ff=False

    for i in range(1,n):
      nxtl[i]+=nxtl[i-1]

    if ff:
      return ' '.join(str(x) for x in l)

    l=nxtl

    # print(l)

  return ' '.join(str(x) for x in l)

# main()
print(main())
