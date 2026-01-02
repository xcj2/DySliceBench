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
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N,A,B,C,D = I()
maze = s()
Flag = 0
for i in range(A,max(C,D)):
    if maze[i-1:i+1] == '##':
        print('No')
        exit()
if C < D:
    print('Yes')
    exit()
for i in range(B-1,D):
    if maze[i-1:i+2] == '...':
        print('Yes')
        exit()
print('No')