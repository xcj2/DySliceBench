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

N,M = map(int,input().split())
found = 0

check_list = []
for j in range(M):
  check_list.append(tuple(map(int,input().split())))

if N > 1:
  for i in range(pow(10,N-1),pow(10,N)):
    if not found:
      is_ok = 1
      for item in check_list:
        s,c = item[0], item[1]
        ss = str(i)
        if ss[s-1] != str(c):
          is_ok = 0
      if is_ok:
        print(i)
        found = 1
        break
      
else:
  for i in range(10):
    if not found:
      is_ok = 1
      for item in check_list:
        s,c = item[0], item[1]
        ss = str(i)
        if ss[s-1] != str(c):
          is_ok = 0
      if is_ok:
        print(i)
        found = 1
        break


if not found:
  print(-1)
        