# coding: utf-8
# submission # - User: herp_sy
# https://atcoder.jp/contests/
#
# lang: Python3 (3.4.3)

import math
import statistics
import numpy as np
import queue

# fact(int)
def fact(n):
  if(n == 1):
    return 1
  else:
    return (n * fact(n - 1))

# gcd(int,int)
def gcd(a,b):
  if a == 0:
    return b
  elif b == 0:
    return a
  else:
    return gcd(b,a % b)

# lcm(int,int)
def lcm(a,b):
  return (a * b / gcd(a,b))

# qsort(array[])
def qsort(seq):
  if len(seq) < 1:
      return seq
  pivot = seq[0]
  left = []
  right = []
  for x in range(1, len(seq)):
    if seq[x] <= pivot:
        left.append(seq[x])
    else:
        right.append(seq[x])
  left = qsort(left)
  right = qsort(right)
  foo = [pivot]
  return (left + foo + right)

# = map(int, input().split())
# = int(input())
# = raw_input().split()
# = list(int(i) for i in input().split())

h = int(input())
w = int(input())
n = int(input())

if n / h > n / w:
  print(math.ceil(n / w))
else:
  print(math.ceil(n / h))
