import math
import fractions
import bisect
import collections
import itertools
import heapq
import string
import sys
import copy
from collections import deque
sys.setrecursionlimit(10**7)
def gcd(a,b):return fractions.gcd(a,b) #最大公約数
def lcm(a,b):return (a*b) // fractions.gcd(a,b) #最小公倍数
def iin(): return int(input()) #整数読み込み
def isn(): return input().split() #文字列読み込み
def imn(): return map(int, input().split()) #整数map取得
def iln(): return list(map(int, input().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def perm_count(n, r): return math.factorial(n) // math.factorial(n-r) # 順列の総数
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def comb_count(n, r): return math.factorial(n) // (math.factorial(n-r) * math.factorial(r)) #組み合わせの総数

N,W = imn()
max_v = 100001
wv = [iln() for _ in range(N)]
max_w = 10**10
dp = [[max_w for _ in range(max_v+1)] for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for sum_v in range(max_v):
        if sum_v - wv[i][1] >= 0:
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v-wv[i][1]]+wv[i][0])
        dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])

ans = 0
for sum_v in range(max_v):
    if dp[N][sum_v] <= W: ans = sum_v
print(ans)