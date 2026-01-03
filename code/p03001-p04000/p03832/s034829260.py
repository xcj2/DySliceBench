#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
  return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

#互いに素なa,bについて、a*x+b*y=1の一つの解[x,y]を出力
def extgcd(a,b):
  r = [1,0,a]
  w = [0,1,b]
  while w[2]!=1:
    q = r[2]//w[2]
    r2 = w
    w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
    r = r2
    w = w2
  return [w[0],w[1]]

# aの逆元(mod M)を求める（aとMは互いに素であることが前提）
def mod_inv(a,M=mod):
  x = extgcd(a,M)[0]
  return (M+x%M)%M

#0!からn!までをmodしつつ計算
def mod_fact(n,Mod=mod):
  d = [1]*(n+1)
  for i in range(1,n+1):
    d[i] = d[i-1]*i%Mod
  return d

N,A,B,C,D = II()

value = [0]
for i in range(C,D+1):
  value.append(i)

fact = mod_fact(N)

inv = [0]*(N+1)
inv[N] = mod_inv(fact[N])
for i in range(1,N+1)[::-1]:
  inv[i-1] = inv[i]*i%mod

dp=[[0]*(N+1) for _ in range(B+1)]
for i in range(B):
  dp[i+1][0] = 1
for i in range(A,B+1):
  for j in range(A,N+1):
    if i==A:
      if j%A!=0:
        continue
      else:
        num = j//A
        if C<=num<=D:
          dp[i][j] = (fact[N]*inv[N-j]*inv[num]*pow(inv[A],num,mod))%mod
    else:
      for k in value:
        if k>j//i:
          break
        else:
          dp[i][j] = (dp[i][j] + dp[i-1][j-i*k]*fact[N-j+i*k]*inv[N-j]*pow(inv[i],k,mod)*inv[k])%mod
print(dp[B][N])