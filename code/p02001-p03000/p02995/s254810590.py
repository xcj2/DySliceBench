import math
import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


DIV = 10**9+7

def ncr(n, r, mod=DIV):
	r = min(r, n-r)
	ret = 1
	for i in range(1, r+1):
		ret = ret * (n-i+1) % mod
		ret = ret * mod_inv(i, mod) % mod
	return ret
    
def mod_modify(a,mod):
    return (a+mod)%mod

def cal_ABC(A,B,C):
    AC = A//C + (1 if A%C>0 else 0)
    BC = (B//C)
    return max(BC-AC+1,0)


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

def main():
    ans =0
    A,B,C,D = ints_raw()
    total = B-A+1
    dC = cal_ABC(A,B,C)
    dD = cal_ABC(A,B,D)
    dCD = cal_ABC(A,B,C*D//gcd(max(C,D),min(C,D)))
    return total-dC-dD+dCD

print(main())
