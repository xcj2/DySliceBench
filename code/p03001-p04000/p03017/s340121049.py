# -*- coding: utf-8 -*-
import sys;
import string;
sys.setrecursionlimit(20000) # 再起呼び出しの最大数をセット

import copy
import itertools

from functools import lru_cache
#@lru_cache(maxsize = None)

# 整数の入力
#n = int(input())

# スペース区切りの整数の入力
#a = [x for x in map(int, input().split())]
n, a, b, c, d = map(int, input().split())
#print("sp", n, q, file=sys.stderr)

# 改行区切りの整数の入力
#a = []
#for x in range(m):
#  a.append([int(x) for x in input().split()])
#p = [int(x) for x in input().split()]

# 文字列の入力
s = input()

# 出力
#print("{} {}".format(a+b+c, s))
#a.sort()
#print(set(a), file=sys.stderr)
#print(len(set(a)))

#cache = dict()

a -= 1
b -= 1
c -= 1
d -= 1

def canswap(s, b, d):
  print("canswap", s, file=sys.stderr)
  for x in range(b, d + 1):
    #print(x, file=sys.stderr)
    prev = s[x - 1] != '#'
    curr = s[x] != '#'
    post = s[x + 1] != '#'
    print(prev, post, file=sys.stderr)
    if post and prev and curr:
      return True
  return False

def canmove(s, a, c):
  print(s, file=sys.stderr)
  if a + 1 == c:
    return s[a + 1] != '.'
  prev = s[a + 1] != '.'
  for x in range(a + 2, c):
    #print(x, file=sys.stderr)
    post = s[x] != '.'
    if post and prev:
      return False
    prev = post
      
  return True

def doit():  
  s2 = list(s)
  print(s2, file=sys.stderr)
  s2[a] = 'A'
  s2[b] = 'B'
  print('s2 ', s2, file=sys.stderr)

  res = list(s)
  res[c] = 'A'
  res[d] = 'B'
  print('res', res, file=sys.stderr)
  
  if c < d:
    if not canmove(s2, b, d):
      return False
    s2[b] = '.'
    s2[d] = 'B'
    return canmove(s2, a, c)
  else:
    if not canmove(s2, a, c):
      if not canswap(s2, b, d):
        return False
      else:
        s2[b] = '.'
        return canmove(s2, a, c)
    s2[a] = '.'
    s2[c] = 'A'
    return canmove(s2, b, d)

#print(doit([0] * 4))
#doit()
try:
  print('Yes' if doit() else 'No')
    
except Exception as e:
  print("e", e, file=sys.stderr)
