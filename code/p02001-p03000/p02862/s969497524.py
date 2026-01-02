import sys
import itertools
import math
from math import factorial
from heapq import heapify, heappop, heappush
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k]) %mod

    return result

X, Y = IL()

num = 0
n = 0
f = 0
for i in range(X+1): #(1, 2)を取る回数
  x = X - i
  y = Y - 2*i
  if x == 2*y:
    n = i
    num = i + y
    f = 1
    break
if f == 0:
  print(0)
else:
  print(cmb(num, n) %mod)