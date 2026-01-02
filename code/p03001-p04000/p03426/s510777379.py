from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1000000)
INF = 10**10

(H, W, D) = reads()
L = W * H

inv = [None] * L


for j in range(H):
    A = reads()
    for i in range(W):
        inv[A[i]-1] = (i, j)

psum = [0] * L

def dist(p, q):
    (x, y) = p
    (z, w) = q
    return abs(y-w) + abs(z-x)

for i in range(D, L):
    psum[i] = psum[i-D] + dist(inv[i], inv[i-D])

# print(psum, file=stderr)

Q = read()

for i in range(Q):
    (L, R) = reads()
    print(psum[R-1] - psum[L-1])
