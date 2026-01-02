# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import math
from functools import lru_cache

#############
# Constants #
#############

MOD = 10**9 +7
INF = float('inf')

#############
# Functions #
#############

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

#############
# Main Code #
#############

N,P = map(int,input().split())
S = list(input())


mods = [0 for _ in range(P)]
count = 0

loop = 0
mod = 0

if P != 2 and P != 5: 
  for digit in S[::-1]:
    loop += 1
    digit = int(digit)
    mod = (mod + digit*pow(10,loop-1,P))%P
    count += mods[mod]
    mods[mod] += 1
    if mod == 0:
      count += 1
else:
  for digit in S:
    loop += 1
    if int(digit)%P == 0:
      count += loop


  

print(count)
