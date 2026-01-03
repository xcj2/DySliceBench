import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools,pdb
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N, K = LI()
D = LI()
nums = [str(i) for i in range(0, 10) if i not in D]

"""
使える数字の中で一番低いものから試していく
見つかったら各桁試していく

"""

all_nums = []
for i in range(N, 99999):
    # 全数字の列挙
    all_nums.append(i)
for num in all_nums:
    if num >= N:
        if all(i in nums for i in str(num)):
            print(num)
            exit()



