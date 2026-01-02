import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

A, B, C = LI()

nums = sorted([A,B,C])
set_nums = list(set([A,B,C]))
result = 0
if len(set_nums) == 1:
    print(0)
elif len(set_nums) == 2:
    # 2種類は一緒
    #前２つが一緒かつはぐれが大きい
    if nums[0] == nums[1]:
        result += nums[2]-nums[1]
        print(result)
        exit()
    elif nums[1] == nums[2]:
        # 後ろ２つが等しく、はぐれが最小
        result += (nums[1] - nums[0])//2
        if (nums[1]-nums[0]) % 2 != 0:
            result += 2
        print(result)
        exit()
else:
    # 全数字が異なる
    result += nums[2]-nums[1]
    nums[0] += nums[2]-nums[1]
    result += (nums[2] - nums[0]) // 2
    if (nums[2] - nums[0]) % 2 != 0:
        result += 2

    print(result)

