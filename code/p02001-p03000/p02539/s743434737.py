# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

import math
#from math import gcd
import bisect
import heapq
from collections import defaultdict
from collections import deque
from collections import Counter
from functools import lru_cache

#############
# Constants #
#############

MOD = 998244353
INF = float('inf')
AZ = "abcdefghijklmnopqrstuvwxyz"

#############
# Functions #
#############

######INPUT######
def I(): return int(input().strip())
def S(): return input().strip()
def IL(): return list(map(int,input().split()))
def SL(): return list(map(str,input().split()))
def ILs(n): return list(int(input()) for _ in range(n))
def SLs(n): return list(input().strip() for _ in range(n))
def ILL(n): return [list(map(int, input().split())) for _ in range(n)]
def SLL(n): return [list(map(str, input().split())) for _ in range(n)]


#####Shorten#####
def DD(arg): return defaultdict(arg)

#####Inverse#####
def inv(n): return pow(n, MOD-2, MOD)

######Combination######
kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n): return kaijo_memo[n]
  if(len(kaijo_memo) == 0): kaijo_memo.append(1)
  while(len(kaijo_memo) <= n): kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n): return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0): gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n): gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if n == r: return 1
  if n < r or r < 0: return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

######Factorization######
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0: 
        cnt+=1 
        temp //= i
      arr.append([i, cnt])
  if temp!=1: arr.append([temp, 1])
  if arr==[]: arr.append([n, 1])
  return arr

#####MakeDivisors######
def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i: 
        divisors.append(n//i)
  return divisors

#####MakePrimes######
def make_primes(N):
  max = int(math.sqrt(N))
  seachList = [i for i in range(2,N+1)]
  primeNum = []
  while seachList[0] <= max:
    primeNum.append(seachList[0])
    tmp = seachList[0]
    seachList = [i for i in seachList if i % tmp != 0]
  primeNum.extend(seachList)
  return primeNum

#####GCD#####
def gcd(a, b):
    while b: a, b = b, a % b
    return a

#####LCM#####
def lcm(a, b):
    return a * b // gcd (a, b)

#####BitCount#####
def count_bit(n):
  count = 0
  while n:
    n &= n-1
    count += 1
  return count

#####ChangeBase#####
def base_10_to_n(X, n):
  if X//n: return base_10_to_n(X//n, n)+[X%n]
  return [X%n]

def base_n_to_10(X, n):
  return sum(int(str(X)[-i-1])*n**i for i in range(len(str(X))))

def base_10_to_n_without_0(X, n):
  X -= 1
  if X//n: return base_10_to_n_without_0(X//n, n)+[X%n]
  return [X%n]

#####IntLog#####
def int_log(n, a):
  count = 0
  while n>=a:
    n //= a
    count += 1
  return count

#############
# Main Code #
#############

ROOT = 3
MOD = 998244353
roots  = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(24)] # 1 の 2^i 乗根
iroots = [pow(x,MOD-2,MOD) for x in roots] # 1 の 2^i 乗根の逆元

def untt(a,n):
  for i in range(n):
    m = 1<<(n-i-1)
    for s in range(1<<i):
      w_N = 1
      s *= m*2
      for p in range(m):
        a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m])%MOD, (a[s+p]-a[s+p+m])*w_N%MOD
        w_N = w_N*roots[n-i]%MOD

def iuntt(a,n):
  for i in range(n):
    m = 1<<i
    for s in range(1<<(n-i-1)):
      w_N = 1
      s *= m*2
      for p in range(m):
        a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]*w_N)%MOD, (a[s+p]-a[s+p+m]*w_N)%MOD
        w_N = w_N*iroots[i+1]%MOD
      
  inv = pow((MOD+1)//2,n,MOD)
  for i in range(1<<n):
    a[i] = a[i]*inv%MOD

def convolution(a,b):
  la = len(a)
  lb = len(b)
  deg = la+lb-2
  n = deg.bit_length()
  if min(la, lb) <= 50:
    if la < lb:
      la,lb = lb,la
      a,b = b,a
    res = [0]*(la+lb-1)
    for i in range(la):
      for j in range(lb):
        res[i+j] += a[i]*b[j]
        res[i+j] %= MOD
    return res

  N = 1<<n
  a += [0]*(N-len(a))
  b += [0]*(N-len(b))
  untt(a,n)
  untt(b,n)
  for i in range(N):
    a[i] = a[i]*b[i]%MOD
  iuntt(a,n)
  return a[:deg+1]
  
N = I()

nokori = [1]
for n in range(1,2*N+10):
  nokori.append((nokori[-1]*(2*n-1)*(2*n)*inv(2)*inv(n))%MOD)

dic = DD(int)
for _ in range(N*2):
  dic[I()] += 1
A = [dic[k] for k in dic]
  
P = []
for a in A:
  temp = 1
  count = 0
  P.append([temp])
  while a >= 2:
    temp *= a*(a-1)//2
    temp %= MOD
    count += 1
    P[-1].append((temp*gyaku_kaijo(count))%MOD)
    a -= 2

Q = deque(P)
while len(Q)>1:
  p = Q.popleft()
  q = Q.popleft()
  Q.append(convolution(p, q))
Q = list(Q[0])
  
ans = 0
M = len(Q)

def sign(x):
  if x%2: return -1
  else: return 1

for i in range(M):
  ans += sign(i) * Q[i] * nokori[N-i]
  ans %= MOD
  
print(ans)
