from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

def solve(A, B, C, D):
  if A < B or D < B:
    print("  V1", file=stderr)
    return False
  CC = C + 1
  if B <= CC:
    print("  V2", file=stderr)
    return True
  g = gcd(D, B)
  # [CC, B) is prohobited
  if CC <= B - g:
    print("  V3", file=stderr)
    return False
  else:
    print("  V4", file=stderr)
    return A % g < CC % g

T = read()
for _ in range(T):
  A, B, C, D = reads()
  print("Yes" if solve(A, B, C, D) else "No")