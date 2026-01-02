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
cnt = 0
for i in range(N):
    if X[i] == '1':
        cnt += 1
cnt1 = cnt+1#0用
cnt2 = cnt-1#1用
nums = []
ans = []
tans = [1]*N
for i in range(N):
    if X[i] == '0':
        nums.append(num1)
    else:
        num3 += num1
        num4 += num2
        nums.append(num2)
    if cnt1 != 0:
        num1 = (num1*2)%cnt1
    if cnt2 != 0:
        num2 = (num2*2)%cnt2
if cnt1 != 0:
    num3 %= cnt1
if cnt2 != 0:
    num4 %= cnt2
for i in range(N):
    if X[i] == '0':
        if cnt1 != 0: 
            ans.append((num3+nums[i])%cnt1)
        else:
            ans.append(0)
            tans[i] = 0
    else:
        if cnt2 != 0:    
            ans.append((num4-nums[i])%cnt2)
        else:
            ans.append(0)
            tans[i] = 0
ans.reverse()
tans.reverse()
def f(n):
    if n == 0:
        return
    tans[i] += 1
    c = n%(list(bin(n)[2:]).count('1'))
    f(c)
for i in range(N):
    f(ans[i])
for i in range(N):
    print(tans[i])