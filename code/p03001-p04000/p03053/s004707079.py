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
MOD = 10**9+7
def gcd(a,b):return fractions.gcd(a,b) #最大公約数
def lcm(a,b):return (a*b) // fractions.gcd(a,b) #最小公倍数
def iin(): return int(input()) #整数読み込み
def ifn(): return float(input()) #浮動小数点読み込み
def isn(): return input().split() #文字列読み込み
def imn(): return map(int, input().split()) #整数map取得
def fmn(): return map(float, input().split()) #浮動小数点map取得
def iln(): return list(map(int, input().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def fln(): return list(map(float, input().split())) # 浮動小数点リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def perm_count(n, r): return math.factorial(n) // math.factorial(n-r) # 順列の総数
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def comb_count(n, r): return math.factorial(n) // (math.factorial(n-r) * math.factorial(r)) #組み合わせの総数
def two_distance(a, b, c, d): return ((c-a)**2 + (d-b)**2)**.5 # 2点間の距離
def m_add(a,b): return (a+b) % MOD

H, W = imn()
count = [[-1 for _ in range(W)] for _ in range(H)]
queue = deque([])
A = []
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == '#': 
            queue.append((i,j))
            count[i][j] = 0
    A.append(list(s))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0
while len(queue) > 0:
    point = queue.popleft()
    for i in range(4):
        x = point[1] + dx[i]
        y = point[0] + dy[i]
        if x < 0 or x >= W or y < 0 or y >= H: continue
        if count[y][x] != -1: continue
        count[y][x] = count[point[0]][point[1]] + 1
        queue.append((y,x))
        ans = max(ans, count[y][x])
print(ans)