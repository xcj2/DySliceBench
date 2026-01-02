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
h = inpl()
dp = [INF] * (n)
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(n-2):
    left = dp[i + 1] + abs(h[i + 2] - h[i + 1])
    right = dp[i] + abs(h[i + 2] - h[i])
    dp[i + 2] = min(left, right)
print(dp[n-1])