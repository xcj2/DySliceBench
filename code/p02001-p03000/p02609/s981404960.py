import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
fact = math.factorial
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

N = i()
X = s()[::-1]
num1 = 1
num2 = 1
num3 = 0
num4 = 0
cnt = X.count('1')
cnt1 = cnt+1#0用
cnt2 = cnt-1#1用
nums1 = []
nums2 = []
ans = [1]*N

for i in range(N):
    if X[i] == '0':
        nums1.append(num1)
    else:
        num3 += num1
        num4 += num2
        nums1.append(num2)
    if cnt1 != 0:
        num1 = (num1*2)%cnt1
    if cnt2 != 0:
        num2 = (num2*2)%cnt2

for i in range(N):
    if X[i] == '0':
        if cnt1 != 0: 
            nums2.append((num3+nums1[i])%cnt1)
        else:
            nums2.append(0)
            ans[i] = 0
    else:
        if cnt2 != 0:    
            nums2.append((num4-nums1[i])%cnt2)
        else:
            nums2.append(0)
            ans[i] = 0
nums2.reverse()
ans.reverse()

def p(n):
    if n == 0:
        return
    ans[i] += 1
    c = n%(bin(n).count('1'))
    p(c)

for i in range(N):
    p(nums2[i])
for i in range(N):
    print(ans[i])