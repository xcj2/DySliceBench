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


a, b, c = inpl()
k = inp()
FLAG = True
while k:
    if b > a:
        FLAG = False
        break
    b *= 2
    k -= 1
if FLAG:
    print("No")
    exit()
FLAG = True
while k:
    if c > b:
        break
    c *= 2
    k -= 1
if FLAG and c <= b:
    print("No")
    exit()
print("Yes")
