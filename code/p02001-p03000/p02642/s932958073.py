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
a = sorted(inpl())
cnt = collections.Counter(a)
ans = 0
dp = [0] * (10**6 + 1)
for i in a:
    if dp[i] == 0:
        for j in range(1, 10**7):
            if i * j > 10**6:
                break
            dp[i * j] = 1
        if cnt[i] == 1:
            ans += 1
print(ans)
