import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  dp=[0]*100010

  n,m=LI()

  dp[0]=1
  dp[1]=1

  for _ in range(m):
    dp[I()]=-1

  for i in range(2,n+1):
    if dp[i]==-1:
      continue

    if dp[i-2]!=-1:
      dp[i]+=dp[i-2]
    if dp[i-1]!=-1:
      dp[i]+=dp[i-1]

    dp[i]%=mod

  return dp[n]%mod

print(main())
