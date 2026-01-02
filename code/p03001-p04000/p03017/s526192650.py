from sys import exit, setrecursionlimit, stderr, stdin
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect
import functools

setrecursionlimit(10**7)

def input():
  return stdin.readline().strip()

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

N, A, B, C, D = reads()
S = input()

def reachable(i, j):
  return not any(S[k] == S[k+1] == "#" for k in range(i, j))

def swappable(i, j):
  return any(S[k-1] == S[k] == S[k+1] == "." for k in range(i, j+1))

A, B, C, D = A-1, B-1, C-1, D-1

possible = reachable(A, C) and reachable(B, D)

if D < C:
  # A < B < D < C
  swapl = swappable(B, D)
  possible = possible and swapl

print("Yes" if possible else "No")