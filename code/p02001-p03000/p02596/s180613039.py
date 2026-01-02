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


x = 7
ans = 1
k = inp()
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()
while True:
    if x % k == 0:
        print(ans)
        exit()
    else:
        x += 7 * pow(10, ans, k) % k
        ans += 1
