# https://atcoder.jp/contests/arc026/tasks/arc026_2
import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

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
  d,g=LI()
  l=[LI() for _ in range(d)]

  ans=inf
  for i in range(2**d):
    sm=0
    cnt=0
    _l=[0]*d
    for j in range(d):
      if i&(1<<j):
        cnt+=l[j][0]
        sm+=l[j][0]*(j+1)*100+l[j][1]
        _l[j]=1

    if sm<g:
      while True:
        for k in range(d)[::-1]:
          if _l[k]==0:
            _l[k]=2 # for debug
            if sm+(k+1)*100*(l[k][0]-1)>=g:
              _cnt=(g-sm+(k+1)*100-1)//((k+1)*100)
              cnt+=_cnt
              sm+=_cnt*(k+1)*100
              break
            else:
              cnt+=l[k][0]-1
              sm+=(k+1)*100*(l[k][0]-1)

        break

    if sm>=g:
      ans=min(ans,cnt)

    # print(cnt,sm,_l)

  return ans

# main()
print(main())
