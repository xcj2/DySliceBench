# データ読み込み

import sys
from collections import deque

def input_data(d=""):
  t = sys.stdin.read()
  if t:
    return t
  else:
    if d[0] == "\n":
      d = d[1:]
    if d[-1] == "\n":
      d = d[:-1]    
    return d

A, *B  = map(int,input_data().split())

def aaa(k):
  k = int(k)
  if A == k:
    if A % 2 == 1:
      return 0
    k = int(k // 2)
  if k == 0:
    return 0
  return int(k//5) + aaa(k//5)

def bbb(k):
  k = int(k)
  if A == k:
    if A % 2 == 1:
      return int(0)
    k = int(k / 2)
  if k == 0:
    return 0
  return int(k/2) + bbb(k/2)

print(min([aaa(A)]))
