# python3.4.2用
import math
import fractions
import collections
import itertools
import heapq
import string
import sys
import copy
import numpy as np
from decimal import *
from collections import deque
sys.setrecursionlimit(10**7)
MOD = 10**9+7
INF = float('inf') #無限大
def gcd(a,b):return fractions.gcd(a,b) #最大公約数
def lcm(a,b):return (a*b) // fractions.gcd(a,b) #最小公倍数
def iin(): return int(sys.stdin.readline()) #整数読み込み
def ifn(): return float(sys.stdin.readline()) #浮動小数点読み込み
def isn(): return sys.stdin.readline().split() #文字列読み込み
def imn(): return map(int, sys.stdin.readline().split()) #整数map取得
def imnn(): return map(lambda x:int(x)-1, sys.stdin.readline().split()) #整数-1map取得
def fmn(): return map(float, sys.stdin.readline().split()) #浮動小数点map取得
def iln(): return list(map(int, sys.stdin.readline().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def fln(): return list(map(float, sys.stdin.readline().split())) # 浮動小数点リスト取得
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def perm_count(n, r): return math.factorial(n) // math.factorial(n-r) # 順列の総数
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def two_distance(a, b, c, d): return ((c-a)**2 + (d-b)**2)**.5 # 2点間の距離
def m_add(a,b): return (a+b) % MOD
def lprint(l): print(*l, sep='\n')

N = iin()
A = np.array(sys.stdin.readline().split(), np.int64)

two_factor = 1
ans = 0
for i in range(60):
    B = A >> i & 1
    ones = np.count_nonzero(B)
    zeros = N - ones
    zeroone_cmb = ones*zeros%MOD
    ans = (ans + (zeroone_cmb*two_factor%MOD))%MOD
    two_factor = (two_factor*2)%MOD

print(ans)
    
