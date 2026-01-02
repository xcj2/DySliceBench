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


class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size
        self.total = 0

    def add(self, i, w):
        x = i + 1
        self.total += w
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res


def inv_cnt(seq):
    n = len(seq)
    bit = BIT(n)
    cnt = 0
    for i in range(n - 1, -1, -1):
        cnt += bit.sum(seq[i] - 1)
        bit.add(seq[i], 1)
    return cnt


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
        ans = min(ans, inv_cnt(whole_idx_list))

if ans == INF:
    print(-1)
else:
    print(ans)


