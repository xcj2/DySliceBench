# -*- coding: utf-8 -*-
import sys;
import string;
sys.setrecursionlimit(20000) # 再起呼び出しの最大数をセット

import copy
import math
import itertools

from functools import lru_cache
#@lru_cache(maxsize = None)

PPP = 1000000007

# 整数の入力
n = int(input())

# スペース区切りの入力
#n, x = input().split()

# スペース区切りの整数の入力
#a, b = map(int, input().split())
#n, x = map(int, input().split())
#print("sp", n, k, file=sys.stderr)
p = [int(x) for x in input().split()]
#b = [int(x) for x in input().split()]
#print("a", a, file=sys.stderr)
#p, q, r = map(int, input().split())
#s = [int(x) for x in input().split()]
#t = [int(x) for x in input().split()]

# 改行区切りの整数の入力
#a = []
#for x in range(n):
#  a.append(int(input()))
#  a.append([int(x) for x in input().split()])
#b = []
#for x in range(m):
#  b.append([int(x) for x in input().split()])
#p = [int(x) for x in input().split()]
#a.sort()
#print(l, file=sys.stderr)

# 文字列の入力
#s = input()

# 出力
#print("{} {}".format(a+b+c, s))
#a.sort()
#print(set(a), file=sys.stderr)
#print(len(set(a)))

#cache = dict()

import re
import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def ton(n, k, x):
  s = ""
  while n > 0:
    s = str(n%k) + s
    n //= k
  return s


#print("a", a, file=sys.stderr)
#print("b", b, file=sys.stderr)

def getEnergy():
  for y in b:
    yield y

def doit():
  ng = 0
  for i in range(n):
    if i + 1 != p[i]:
      ng += 1
  
  print("", ng, file=sys.stderr)
  return ng == 0 or ng == 2

def yn():
  if doit():
    return "YES"
  else:
    return "NO"

#print(doit([0] * 4))
#doit(a)
#print(doit())
try:
  #doit()
  #print(doit())
  print(yn())
except Exception as e:
  print("e", e, file=sys.stderr)
