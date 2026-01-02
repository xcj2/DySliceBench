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

# 2*5 の数が末尾の0の数
# nが奇数だと素因数2は出現しないので0
# 偶数の場合のみ考える
# （掛け合わせる数は全て偶数なので（これって理由になってる？））素因数は2よりも5の方が少ない
# 素因数5の数をカウントする
# （2*5で割れる個数）+（2*25で割れる個数）＋... が答え（2をかけているのは偶数前提なので）

def main():
  n=I()

  if n%2!=0:
    return 0

  a=2
  ans=0
  while True:
    a*=5
    if a>n:
      return ans
    ans+=n//a

# main()
print(main())
