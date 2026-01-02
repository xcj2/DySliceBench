import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


def func(a, b, c):
    return a * a + b * b + c * c + a * b + b * c + c * a


n = inp()
limit = int(math.sqrt(n)) + 1
ans = [0] * n
for i in range(1, limit):
    for j in range(i, limit):
        for k in range(j, limit):
            x = func(i, j, k) - 1
            if x < n:
                if len(set([i, j, k])) == 1:
                    ans[x] += 1
                elif len(set([i, j, k])) == 2:
                    ans[x] += 3
                elif len(set([i, j, k])) == 3:
                    ans[x] += 6
for i in ans:
    print(i)
