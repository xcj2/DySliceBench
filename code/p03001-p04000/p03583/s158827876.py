import sys,collections

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  a=I()

  for h in range(1,3501):
    for n in range(1,3501):
      x=(4*h*n-a*n-a*h)
      if x==0:
        continue
      w=a*h*n/x
      if w>0 and w==int(w) and w<=3500:
        print(h,n,int(w))
        exit()

main()
# print(main())
