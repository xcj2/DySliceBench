# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())
a = [int(i) for i in readline().split()]
b = [int(i) for i in readline().split()]


def op(b,i):
    global ans
    if i == n-1:
        res = (b[i]-a[i])//(b[i-1]+b[0])
        if res < 0: return 0
        b[i] -= (b[i-1]+b[0])*res
    else:
        res = (b[i]-a[i])//(b[i-1]+b[(i+1)])
        if res < 0: return 0
        b[i] -= (b[i-1]+b[(i+1)])*res
    ans += res
    return res

def check(b,c):#c からチェック 操作ができる最初のi
#    print(b,c)
    for i in range(c,c+n):
        if op(b,i%n) > 0: return i
    else:
        return(-1)

def rev(b,i):#iから逆向きに操作
    for j in range(i-1,-n,-1):
#        print(b,j)
        if op(b,j%n) == 0: break

    
c = 0
ans = 0
"""
while True:
    i = check(b,c)
    if i == -1: break
    rev(b,i)
    c += 1
    if c >= n: c -= n
"""

s = set(range(n))

while s:
    i = s.pop()
    if op(b,i) > 0:
        s.add((i-1)%n)
        s.add((i+1)%n)

if a == b:
    print(ans)
else:
    print(-1)










