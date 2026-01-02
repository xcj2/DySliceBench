from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
from functools import lru_cache
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
def inpl_str():
    '''
    一行に複数の文字
    '''
    return list(input().split())

n = inp()
dp = [[0] * 3 for i in range(n+1)]
for i in range(n):
    work = inpl()
    for j in range(3):
        option = [dp[i][k] + work[k] for k in range(3) if j != k]
        dp[i + 1][j] = max(option)
print(max(dp[n]))