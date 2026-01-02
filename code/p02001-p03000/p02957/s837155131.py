# coding: utf-8
# submission # - User: herp_sy
# https://atcoder.jp/contests/

import math
import statistics

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

a,b = map(int, input().split())
#  = int(input())
#  = raw_input().split()
#  = list(int(i) for i in input().split())  

k = (a + b) // 2;
if abs(k - a) == abs(k - b):
  print(k)
else:
  print("IMPOSSIBLE")
