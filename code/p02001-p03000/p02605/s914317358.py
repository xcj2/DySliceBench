# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

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

MOD = 10**9+7
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

######OUTPUT######
def P(arg): print(arg); return
def Y(): print("Yes"); return
def N(): print("No"); return
def E(): exit()
def PE(arg): print(arg); exit()
def YE(): print("Yes"); exit()
def NE(): print("No"); exit()

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

N = I()
data = SLL(N)

Udic = DD(list)
Ddic = DD(list)
Ldic = DD(list)
Rdic = DD(list)

URdic = DD(lambda:[[],[]])
DLdic = DD(lambda:[[],[]])

ULdic = DD(lambda:[[],[]])
DRdic = DD(lambda:[[],[]])

for i in range(N):
  x,y,s = data[i]
  x,y = int(x), int(y)
  if s == "U":
    Udic[x].append(y)
    URdic[x+y][0].append(x)
    ULdic[x-y][0].append(x)
  if s == "D":
    Ddic[x].append(y)
    DLdic[x+y][0].append(x)
    DRdic[x-y][0].append(x)
  if s == "L":
    Ldic[y].append(x)
    DLdic[x+y][1].append(x)
    ULdic[x-y][1].append(x)
  if s == "R":
    Rdic[y].append(x)
    URdic[x+y][1].append(x)
    DRdic[x-y][1].append(x)

col_t = INF

Uk = [k for k in Udic]
Dk = [k for k in Ddic]
Lk = [k for k in Ldic]
Rk = [k for k in Rdic]

UDk = set(Uk)&set(Dk)
LRk = set(Lk)&set(Rk)

for k in UDk:
  Udic[k].sort()
  for d in Ddic[k]:
    p = bisect.bisect(Udic[k],d)
    if p:
      col_t = min(col_t,(d-Udic[k][p-1])*5)
      
for k in LRk:
  Rdic[k].sort()
  for l in Ldic[k]:
    p = bisect.bisect(Rdic[k],l)
    if p:
      col_t = min(col_t,(l-Rdic[k][p-1])*5)
      
      
for k in URdic:
  if URdic[k][0] and URdic[k][1]:
    URdic[k][1].sort()
    for u in URdic[k][0]:
      p = bisect.bisect(URdic[k][1],u)
      if p:
        col_t = min(col_t,(u-URdic[k][1][p-1])*10)

for k in DLdic:
  if DLdic[k][0] and DLdic[k][1]:
    DLdic[k][0].sort()
    for l in DLdic[k][1]:
      p = bisect.bisect(DLdic[k][0],l)
      if p:
        col_t = min(col_t,(l-DLdic[k][0][p-1])*10)  

for k in ULdic:
  if ULdic[k][0] and ULdic[k][1]:
    ULdic[k][1].sort()
    for u in ULdic[k][0]:
      p = bisect.bisect(ULdic[k][1],u)
      if p<len(ULdic[k][1]):
        col_t = min(col_t,(ULdic[k][1][p]-u)*10)
for k in DRdic:
  if DRdic[k][0] and DRdic[k][1]:
    DRdic[k][0].sort()
    for r in DRdic[k][1]:
      p = bisect.bisect(DRdic[k][0],r)
      if p<len(DRdic[k][0]):
        col_t = min(col_t,(DRdic[k][0][p]-r)*10)
        
        
if col_t != INF:
  print(col_t)
else:
  print("SAFE")