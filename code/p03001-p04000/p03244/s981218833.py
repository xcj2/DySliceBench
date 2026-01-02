from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate
import sys



def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


n = I()
num = LI()
even_cnt = Counter([num[i] for i in range(n) if i%2]).most_common()
odd_cnt = Counter([num[i] for i in range(n) if i%2==0]).most_common()

odd_cnt += [(0, 0)]
even_cnt += [(0, 0)]


if len(odd_cnt) == 1:
    print(n - odd_cnt[0][1] - even_cnt[1][1])
elif even_cnt[0][0] != odd_cnt[0][0]:
    print(n - even_cnt[0][1] - odd_cnt[0][1])
else:
    print(min(n - even_cnt[0][1] - odd_cnt[1][1], n - even_cnt[1][1] - odd_cnt[0][1]))