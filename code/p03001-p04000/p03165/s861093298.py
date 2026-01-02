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


s = input()
t = input()
dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
# print(dp[len(s)][len(t)])
ans = []
x = len(s)
y = len(t)
while x > 0 and y > 0:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        x -= 1
        y -= 1
        ans.append(s[x])
print(''.join(ans[::-1]))
