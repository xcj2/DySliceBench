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


n = II()
a = sorted(LI(), reverse=True)
ans = []
s = 0
if all([i < 0 for i in a]):
    tmp = a[0]
    for i in range(1, n):
        ans.append((tmp, a[i]))
        tmp -= a[i]
    print(tmp)
    for i in ans:
        print(i[0], i[1])
else:
    tmp = a[-1]
    for i in range(1, n - 1):
        if a[i] < 0:
            break
        ans.append((tmp, a[i]))
        tmp -= a[i]

    ans.append((max(a), tmp))
    tmp = max(a) - tmp

    for i in range(1, n - 1):
        if a[i] >= 0:
            continue
        ans.append((tmp, a[i]))
        tmp -= a[i]
    print(tmp)
    for i in ans:
        print(i[0], i[1])
