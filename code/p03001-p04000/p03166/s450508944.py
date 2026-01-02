'''
N頂点M辺の有向グラフGの有向パスのうち最長のものを求めよ。
terms:
    2<=N<=10**5
    1<=M<=10**5
    (x_i,y_i)はすべて相異なる
    Gは有向閉路を含まない

input:
    4 5
    1 2
    1 3
    3 2
    2 4
    3 4
output:
    3
'''


from collections import defaultdict,deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
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

n, m = inpl()
v = [[] for _ in range(n)]
for i in range(m):
    a, b = inpl()
    v[a - 1].append(b - 1)
'''
v[0]=[1,2]
v[1]=[3]
v[2]=[1,3]
'''

from functools import lru_cache
@lru_cache(maxsize=None)
def dp(x):
    r = 0
    for i in v[x]:
        r = max(r, dp(i) + 1)
    return r

res = max([dp(i) for i in range(n)])
print(res)