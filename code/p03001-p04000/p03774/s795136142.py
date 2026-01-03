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
student = [LI() for i in range(n)]
checkpoint = [LI() for i in range(m)]
for i in student:
    tmp = INF
    ans = 0
    for index, j in enumerate(checkpoint):
        if abs(i[0] - j[0]) + abs(i[1] - j[1]) < tmp:
            tmp = abs(i[0] - j[0]) + abs(i[1] - j[1])
            ans = index + 1 
    print(ans)
