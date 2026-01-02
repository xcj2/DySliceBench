import math
import fractions
import bisect
import collections
import itertools
import heapq
import string
import sys
import copy
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
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def perm_count(n, r): return math.factorial(n) // math.factorial(n-r) # 順列の総数
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def comb_count(n, r): return math.factorial(n) // (math.factorial(n-r) * math.factorial(r)) #組み合わせの総数
def two_distance(a, b, c, d): return ((c-a)**2 + (d-b)**2)**.5 # 2点間の距離
def m_add(a,b): return (a+b) % MOD
def print_list(l): print(*l, sep='\n')

def sieves_of_e(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i * 2, n+1, i): is_prime[j] = False
    return is_prime

S = list(input())
K = iin()
s = copy.deepcopy(S)
last_update = False
count1 = 0
for si in range(1, len(s)):
    if s[si-1] == s[si]:
        s[si] = '?'
        count1 += 1
        if si == len(s)-1:
            last_update = True
count2 = 0
last_update2 = False
if not last_update and S[0] == S[-1]:
    count2 = 1
    S2 = list('?')
    S2.extend(S[1:])
    for i in range(2, len(S2)):
        if S2[i-1] == S2[i]:
            S2[i] = '?'
            count2 += 1
            if i == len(S2)-1:
                last_update2 = True
if len(S) ==1:
    print(len(S)*K//2)
elif K == 1:
    print(count1)
elif count2 == 0:
    print(K*count1)
else:
    if last_update2:
        count12 = count1+count2
        ans = count12*(K//2)
        if K % 2 == 1: 
            ans+= count1
        print(ans)
    else:
        print(count1 + count2*(K-1))