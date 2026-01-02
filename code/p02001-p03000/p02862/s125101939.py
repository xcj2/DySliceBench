import sys
#import bisect
#from collections import deque
import math

def input():
    return sys.stdin.readline().rstrip('\n')


X,Y = list(map(int, input().split()))

if (2*X-Y) % 3:
    print(0)
    sys.exit()

if (2*Y-X) % 3:
    print(0)
    sys.exit()

M = max((2*X-Y)//3, (2*Y-X)//3)
N = min((2*X-Y)//3, (2*Y-X)//3)

if M<0 or N<0:
    print(0)
    sys.exit()
    
mod = pow(10,9) + 7

#from scipy.special import comb
#print(comb(M+N,N) % (pow(10,9) + 7))
#print(comb(M+N,N, exact=True)% (pow(10,9) + 7))  causes "RE" at atcoder
#from math import factorial
#print((factorial(M+N)//factorial(M)//factorial(N)))

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

def ohmycomb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

print(ohmycomb(M+N, N, mod))
