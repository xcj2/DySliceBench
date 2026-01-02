#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#拡張ユークリッドとかしらないので、オイラー関数でmodの逆元計算して無理やり通します。
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
a,b = LI()
g = gcd(a,b)
a//=g
b//=g
if b == 1:
    print(0,1)
    quit()
if b < 4:
    f = b-1
else:
    p = []
    x = 2
    m = b
    while x**2 <= b:
        if not m%x:
            p.append(x)
            while not m%x:
                m//=x
        x += 1
    if m != 1:p.append(m)
    f = b
    for i in p:
        f *= (1-1/i)
    f = int(f)
x_ = pow(a,f-1,b)
y_ = (1-a*x_)//b
ans = [x_,y_,abs(x_)+abs(y_)]
for i in range(-100,100):
    s = -b*i+x_
    t = a*i+y_
    m = abs(s)+abs(t)
    if m < ans[2]:
        ans = [s,t,m]
    elif m == ans[2] and s <= t:
        ans = [s,t,m]
print(ans[0],ans[1])

