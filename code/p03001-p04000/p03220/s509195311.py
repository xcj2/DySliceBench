import sys
import math
import itertools
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
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
import bisect

N = i()
T,A = I()
H = l()
h = copy(H)
H.sort()
B = (T-A)/0.006
i = bisect.bisect_left(H,B)
if  abs((T-H[i-1]*0.006)-A)> abs(A-(T-H[i]*0.006)):
    print(h.index(H[i])+1)
else:
    print(h.index(H[i-1])+1)