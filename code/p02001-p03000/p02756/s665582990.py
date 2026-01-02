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

S = str(input())
Q = int(input())

head = []
tail = []
main = []

main = list(S)

status = 0

def query():
  global head
  global tail
  global main
  global status
  l = list(map(str,input().split()))
  if l[0] == "1":
    status = (status+1)%2
  else:
    letter = l[2]
    if l[1] == "1":
      if status == 0:
        head.append(letter)
      else:
        tail.append(letter)
    else:
      if status == 0:
        tail.append(letter)
      else:
        head.append(letter)

      


while Q:
  Q -= 1
  query()

if status == 0:
  print("".join(head[::-1])+"".join(main)+"".join(tail))
else:
  print("".join(tail[::-1])+"".join(main[::-1])+"".join(head))
  
