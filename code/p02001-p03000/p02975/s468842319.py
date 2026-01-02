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

# スペース区切りの整数の入力
a = [int(x) for x in input().split()]
print("a", a, file=sys.stderr)
#n, d = map(int, input().split())
#print("sp", n, k, file=sys.stderr)
#p, q, r = map(int, input().split())
#s = [int(x) for x in input().split()]
#t = [int(x) for x in input().split()]

# 改行区切りの整数の入力
#a = []
#for x in range(n):
#  a.append(int(input()))
#  a.append([int(x) for x in input().split()])
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

a.sort()
def doloop():
  res = 0
  for x in a:
    res ^= x
  
  return res == 0

def doit():
  if doloop():
    return "Yes"
  else:
    return "No"

#print(doit([0] * 4))
#doit(s)
#print(doit())
try:
  print(doit())
except Exception as e:
  print("e", e, file=sys.stderr)
