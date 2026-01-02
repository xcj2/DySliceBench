from math import *
from heapq import *

def mi():
    return map(int, input().split())
def ii():
    return int(input())
def li():
    return list(mi())
def gcd(a,b):return a if(not b) else gcd(b,a%b)
def qw(a,b,p):
    '''quick pow'''
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % p
        a = a * a % p
        b >>= 1
    return ans
def is_prime(x):
    if(x < 2): return 0
    for i in range(2,int(sqrt(x)+1)):
        if(x % i == 0) : return 0
    return 1

n = ii()
a = li()
ans = 1
ok = 1
a.sort()
for i in range(0,n):
    ans = ans * a[i]
    if(ans > 1000000000000000000):
        ok = 0
        break
# print(ans)
if(ok == 0):print(-1)
else: print(ans)



