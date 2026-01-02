#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
#1_A
"""
import math

n = int(input())
m = n
ans = []
i = 2
k = math.sqrt(n)
while i <= k:
    if n%i == 0:
        n = n//i
        ans.append(i)
        i -= 1
        if n == 1:
            break
    i += 1
if len(ans) == 0 or n != 1:
    ans.append(n)
print(m,end = ": ")
for i in range(len(ans)-1):
    print(ans[i], end = " ")
print(ans[-1])
"""

#1_B
"""
m,n = map(int, input().split())
b = bin(n)[2:]
num = [m]
for i in range(len(b)-1):
    num.append(num[-1]**2%1000000007)
ans = 1
for i in range(len(b)):
    ans *= num[i] if b[len(b)-1-i] == "1" else 1
    ans %= 1000000007
print(ans)
"""

#1_C
"""
import math

l = int(input())
a = list(map(int, input().split()))
dict = {}
for n in a:
    ans = []
    i = 2
    k = math.sqrt(n)
    dic = {}
    while i <= k:
        if n%i == 0:
            n = n//i
            ans.append(i)
            i -= 1
            if n == 1:
                break
        i += 1
    if len(ans) == 0 or n != 1:
        ans.append(n)
    for i in ans:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.keys():
        if i in dict:
            dict[i] = max(dict[i], dic[i])
        else:
            dict[i] = dic[i]
sum = 1
for x,y in dict.items():
    sum *= x**y
print(sum)
"""

#1_D
"""
import math

n = int(input())
m = n
ans = []
i = 2
k = math.sqrt(n)
dic = {}
while i <= k:
    if n%i == 0:
        n = n//i
        ans.append(i)
        i -= 1
        if n == 1:
            break
    i += 1
if len(ans) == 0 or n != 1:
    ans.append(n)
ans = list(set(ans))
sum = m
for i in ans:
    sum *= (1-1/i)
print(int(sum))
"""

#1_E
"""
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
for i in range(-10000,10000):
    s = -b*i+x_
    t = a*i+y_
    m = abs(s)+abs(t)
    if m < ans[2]:
        ans = [s,t,m]
    elif m == ans[2] and s <= t:
        ans = [s,t,m]
print(ans[0],ans[1])
"""

#2
#2_A
"""
a,b = LI()
print(a+b)
"""
#2_B
a,b = LI()
print(a-b)

