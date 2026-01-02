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

a,b,c = list(map(int,input().split()))
d,e,f = list(map(int,input().split()))
g,h,i = list(map(int,input().split()))

bingo = [a,b,c,d,e,f,g,h,i]


check = [0,0,0,0,0,0,0,0,0]

N = int(input())
for i in range(N):
  z = int(input())
  for j in range(9):
    if bingo[j] == z:
      check[j] = 1
      
is_bingo = 0

if check[0] and check[1] and check[2]:
  is_bingo = 1
if check[3] and check[4] and check[5]:
  is_bingo = 1
if check[6] and check[7] and check[8]:
  is_bingo = 1
if check[0] and check[3] and check[6]:
  is_bingo = 1
if check[1] and check[4] and check[7]:
  is_bingo = 1
if check[2] and check[5] and check[8]:
  is_bingo = 1
if check[0] and check[4] and check[8]:
  is_bingo = 1
if check[2] and check[4] and check[6]:
  is_bingo = 1

  
if is_bingo:
  print("Yes")
else:
  print("No")