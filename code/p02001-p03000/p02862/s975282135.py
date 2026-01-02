import sys
import math
input = sys.stdin.readline

def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

mod = 10**9 + 7

x, y = map(int, input().split())

x_ = max(x, y)
y = min(x, y)
x = x_

cnt_x = 0
while 2*x > y and x > 0 and y>0:
    x -= 2
    y -= 1
    cnt_x += 1

if x==-1:
    x += 2
    y += 1

if 2*x == y:
    cnt_y = x

    n = cnt_x + cnt_y 
    k = cnt_y
    print(comb(n, k, mod))

else:
    print(0) 