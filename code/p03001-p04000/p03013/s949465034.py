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


n, m = MI()
a = [II() for _ in range(m)]

tmp = [0] * (n+1)
ok = [True] * (n+1)
for num in a:
    ok[num] = False
tmp[0] = 1
for i in range(n):
    for j in range(i+1, min(n, i+2)+1):
        if ok[j]:
            tmp[j] += tmp[i]
print(tmp[n] % MOD)
