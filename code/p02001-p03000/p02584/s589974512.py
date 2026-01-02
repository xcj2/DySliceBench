import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
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
INF = 10**9
mod = 10**9+7

X,K,D = I()
if X >= 0:
    if K*D <= X:
        print(abs(X-K*D))
        exit()
    num1 = X-(X//D)*D
    num2 = num1-D
    if (X//D)%2 == 0:
        f = 0
    else:
        f = 1
    if (X//D)%2 != (K-X//D)%2:
        if f == 0:
            f = 1
        else:
            f = 0
    if f == 0:
        print(abs(num1))
    else:
        print(abs(num2))
else:
    X *= -1
    if K*D <= X:
        print(abs(X-K*D))
        exit()
    num1 = X-(X//D)*D
    num2 = num1-D
    if (X//D)%2 == 0:
        f = 0
    else:
        f = 1
    if (X//D)%2 != (K-X//D)%2:
        if f == 0:
            f = 1
        else:
            f = 0
    if f == 0:
        print(abs(num1))
    else:
        print(abs(num2))