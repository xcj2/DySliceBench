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


n = inp()
a = inpl()
l = [0] * (n + 1)
r = [0] * (n + 1)
l[0] = 1 - a[0]
for i in range(1, n + 1):
    l[i] = l[i - 1] * 2 - a[i]
for i in range(n - 1, -1, -1):
    r[i] = r[i + 1] + a[i + 1]
ans = 0
for i in range(n + 1):
    if min(l[i], r[i]) < 0:
        print(-1)
        exit()
    ans += min(l[i], r[i]) + a[i]
# print(l)
# print(r)
print(ans)
