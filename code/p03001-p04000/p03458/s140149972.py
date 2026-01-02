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

# A:product
'''
data = input("")
data = data.split(" ")
a = int(data[0])
b = int(data[1])

if (a*b)%2 == 1: print("Odd")
else: print("Even")
'''

# B:1 21
'''
data = input()
data = int(data.replace(" ",""))
if data%(data**(1/2)) == 0: print("Yes")
else: print("No")
'''

# C:Traveling
'''
n = int(input(""))
data = [0]*n
t = [0]*n
x = [0]*n
y = [0]*n
flag = 0

for i in range(n):
    data[i] = input("")
    t[i] = int(data[i].split(" ")[0])
    x[i] = int(data[i].split(" ")[1])
    y[i] = int(data[i].split(" ")[2])

for i in range(n):
    if i == 0:
        if x[i]+y[i] > t[i] or (x[i]+y[i]-t[i])%2 != 0:
            print("No")
            flag = 1
            break
    else:
        if abs(x[i]-x[i-1])+abs(y[i]-y[i-1]) > t[i] or (x[i]+y[i]-t[i])%2 != 0:
            print("No")
            flag = 1
            break
if flag == 0:print("Yes")
'''

# D:Checker
def check(y,x,k):
    l = max(0,min(m,x))
    r = max(0,min(m,x+k))
    d = max(0,min(m,y))
    u = max(0,min(m,y+k))
    f[d][l] += 1
    f[d][r] -= 1
    f[u][l] -= 1
    f[u][r] += 1
n,k = LI()
m = k*2
f = [[0]*(m+1) for i in range(m+1)]
for i in range(n):
    x,y,c = input().split()
    x = int(x)%m
    y = int(y)%m
    if c == "W":
        y += k
        y %= m
    check(y-m+1,x-m+1,k)
    check(y+1,x-m+1,k)
    check(y-k+1,x-k+1,k)
    check(y+k+1,x-k+1,k)
    check(y-m+1,x+1,k)
    check(y+1,x+1,k)
    check(y-k+1,x+k+1,k)
    check(y+k+1,x+k+1,k)

for y in range(m+1):
    for x in range(m):
        f[y][x+1] += f[y][x]

for y in range(m):
    for x in range(m+1):
        f[y+1][x] += f[y][x]

ans = 0
for i in f:
    ans = max(ans,max(i))
print(ans)
