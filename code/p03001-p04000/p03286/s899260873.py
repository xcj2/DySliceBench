# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
#from math import gcd
import bisect
from collections import defaultdict
from collections import deque
from functools import lru_cache


#############
# Constants #
#############

MOD = 10**9+7
INF = float('inf')

#############
# Functions #
#############

######INPUT######
def inputI(): return int(input().strip())
def inputS(): return input().strip()
def inputIL(): return list(map(int,input().split()))
def inputSL(): return list(map(str,input().split()))
def inputILs(n): return list(int(input()) for _ in range(n))
def inputSLs(n): return list(input().strip() for _ in range(n))
def inputILL(n): return [list(map(int, input().split())) for _ in range(n)]
def inputSLL(n): return [list(map(str, input().split())) for _ in range(n)]

######OUTPUT######
def Yes(): print("Yes"); return
def No(): print("No"); return

#####Inverse#####
def inv(n): return pow(n, MOD-2, MOD)

######Combination######
kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n):
    return kaijo_memo[n]
  if(len(kaijo_memo) == 0):
    kaijo_memo.append(1)
  while(len(kaijo_memo) <= n):
    kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n):
    return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0):
    gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n):
    gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if(n == r):
    return 1
  if(n < r or r < 0):
    return 0
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
    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
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

#####LCM#####
def lcm(a, b):
    return a * b // gcd (a, b)

#####BitCount#####
def count_bit(n):
  count = 0
  while n:
    n &= n -1
    count += 1
  return count

#####ChangeBase#####
def Base_10_to_n(X, n):
  if (int(X/n)):
    return Base_10_to_n(int(X/n), n)+[X%n]
  return [X%n]


#############
# Main Code #
#############

N = inputI()


if N >= 0:
  b = Base_10_to_n(N, 2)[::-1]

  ans = [0] * 100
  n = len(b)

  for i in range(n):
    if b[i] == 1:
      if i == 0:
        ans[0] = 1
      else:
        if i%2:
          if ans[i] == 1:
            ans[i] = 0
            continue
          ans[i] += 1
          ans[i+1] += 1
          if ans[i] == 2:
            ans[i] = 0
            ans[i+1] = 1
            ans[i+2] = 1
        else:
          ans[i] += 1
          if ans[i] == 2:
            ans[i] = 0
            ans[i+1] = 1
            ans[i+2] = 1
else:
  b = Base_10_to_n(-N, 2)[::-1]

  ans = [0] * 100
  n = len(b)

  for i in range(n):
    if b[i] == 1:
      if i%2 == 0:
        if ans[i] == 1:
          ans[i] = 0
          continue
        ans[i] += 1
        ans[i+1] += 1
        if ans[i+1] == 2:
          ans[i+1] = 0
          ans[i+2] = 1
          ans[i+3] = 1
      else:
        ans[i] += 1
        if ans[i] == 2:
          ans[i] = 0
          ans[i+1] = 1
          ans[i+2] = 1
  
ans = [str(i) for i in ans]
print(int("".join(ans[::-1])))