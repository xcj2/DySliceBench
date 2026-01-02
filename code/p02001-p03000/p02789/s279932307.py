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
  if len(seq) < 2:
    return seq
  else:
    beg, end = 0, len(seq) - 1
    mid = (beg + end) // 2
    smaller = [c for c in seq if seq[mid] > c]
    equal = [c for c in seq if seq[mid] == c]
    larger = [c for c in seq if seq[mid] < c]
    return (qsort(smaller) + equal + qsort(larger)) 

# = map(int, input().split())
# = int(input())
# = raw_input().split()
# = list(int(i) for i in input().split())

n,m = map(int, input().split())
if n == m:
  print('Yes')
else:
  print('No')
