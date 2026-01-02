import math
from math import factorial
from operator import mul
from functools import reduce
from numpy.linalg import solve
 
X, Y = map(int, input().split())
 
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
 
 
if ((X + Y) %3!=0):
    print(0)
else :
    min_za = min(X, Y)
    max_za = max(X, Y)
    left = [[1, 2],
            [2, 1]]
 
    right = [X, Y]
    diff = (solve(left, right))
    diff_1 = int(diff[0])
    diff_2 = int(diff[1])

    sum = diff_1 + diff_2

    if (diff_1 >=0 and diff_2 >=0):
        print(comb(sum,diff_1,10**9+7))
    else:
        print(0)