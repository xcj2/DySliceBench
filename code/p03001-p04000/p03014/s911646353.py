from collections import Counter
from collections import deque
from functools import reduce
from pprint import pprint
import bisect
import copy
import fractions
import itertools
import math
import queue
import random
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
def GCD_LIST(numbers): return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers): return reduce(LCM, numbers)
def LCM(m, n): return (m * n // fractions.gcd(m, n))


h, w = MI()
s = [IS() for _ in range(h)]
L = [[0 for _ in range(w)] for _ in range(h)]
R = [[0 for _ in range(w)] for _ in range(h)]
D = [[0 for _ in range(w)] for _ in range(h)]
U = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            L[i][j] = 0
        else:
            if j == 0:
                L[i][j] = 1
            elif j > 0:
                L[i][j] = L[i][j - 1] + 1

for i in range(h):
    for j in range(w - 1, -1, -1):
        if s[i][j] == '#':
            R[i][j] = 0
        else:
            if j == w - 1:
                R[i][j] = 1
            elif j < w - 1:
                R[i][j] = R[i][j + 1] + 1

for j in range(w):
    for i in range(h):
        if s[i][j] == '#':
            U[i][j] = 0
        else:
            if i == 0:
                U[i][j] = 1
            elif i > 0:
                U[i][j] = U[i - 1][j] + 1

for j in range(w):
    for i in range(h - 1, -1, -1):
        if s[i][j] == '#':
            D[i][j] = 0
        else:
            if i == h - 1:
                D[i][j] = 1
            elif i < h - 1:
                D[i][j] = D[i + 1][j] + 1

# pprint(L, width=40)
# pprint(R, width=40)
# pprint(U, width=40)
# pprint(D, width=40)

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3, ans)
print(ans)
