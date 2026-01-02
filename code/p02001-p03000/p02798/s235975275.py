from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
import pprint
sys.setrecursionlimit(10 ** 9)


INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n = I()
A = LI()
B = LI()
ans = INF
for odd_ind in combinations(range(n), n // 2):
    even_ind = set(range(n)) - set(odd_ind)
    odd_list = []
    even_list = []
    whole_num_list = []
    whole_idx_list = []
    for i in odd_ind:
        if i % 2:
            odd_list += [(A[i], i)]
        else:
            odd_list += [(B[i], i)]
    for j in even_ind:
        if j % 2:
            even_list += [(B[j], j)]
        else:
            even_list += [(A[j], j)]
    even_list.sort(reverse=1)
    odd_list.sort(reverse=1)
    while even_list or odd_list:
        x, idx = even_list.pop()
        whole_num_list += [x]
        whole_idx_list += [idx]
        if odd_list:
            x, idx = odd_list.pop()
            whole_num_list += [x]
            whole_idx_list += [idx]
    if whole_num_list == sorted(whole_num_list):
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if whole_idx_list[i] > whole_idx_list[j]:
                    cnt += 1
        ans = min(ans, cnt)


if ans == INF:
    print(-1)
else:
    print(ans)


