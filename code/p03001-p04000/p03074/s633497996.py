import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, K = MAP()
S = input()

flg = [S[0]] #各連続部分の数字
count = []   #連続部分の個数
cnt = 1
tmp = S[0]

for x in S[1:]:
	if x == tmp:
		cnt += 1
	else:
		tmp = x
		flg.append(tmp)
		count.append(cnt)
		cnt = 1
count.append(cnt)

count += [0]*(2*K+1)
count = [0] + list(accumulate(count))

ans = 0

for i in range(len(flg)):
	if flg[i] == "1":
		ans = max(ans, count[i+2*K+1] - count[i])
	else:
		ans = max(ans, count[i+2*K] - count[i])

print(ans)

