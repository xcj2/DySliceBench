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
data = collections.defaultdict(int)
for i in range(n):
    data[a[i]] += 1
q = inp()
ans = 0
for key, value in data.items():
    ans += key * value
for i in range(q):
    b, c = inpl()
    ans += (c - b) * data[b]
    data[c] += data[b]
    data[b] = 0
    print(ans)
