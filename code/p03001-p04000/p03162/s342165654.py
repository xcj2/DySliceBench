import sys,io
from functools import lru_cache
import numpy
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())
n=read()
a,b,c=[0]*n,[0]*n,[0]*n
for i,line in enumerate(readlines()):
    a[i],b[i],c[i]=mp(line)
dp=[[0,0,0] for i in range(n+1)]
for k in range(1,n+1):
    one=dp[k-1][1]
    two=dp[k-1][2]
    zero=dp[k-1][0]
    dp[k][0]= one if one >= two else two
    dp[k][0]+=a[k-1]
    dp[k][1]= zero if zero >= two else two
    dp[k][1]+=b[k-1]
    dp[k][2]= one if one >= zero else zero
    dp[k][2]+=c[k-1]
#print(dp)
print(max(dp[n][0],dp[n][1],dp[n][2]))