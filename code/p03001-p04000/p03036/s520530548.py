# coding: utf-8
# user: herp_sy

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

# , = map(int, input.split())
#  = int(input())
x = []
r,d,xs = map(int, input().split())
x.append(xs)
for i in range(0,10):
  x.append(r * x[i] - d)  
  print(x[i + 1])
