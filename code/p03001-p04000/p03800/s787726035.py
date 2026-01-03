import sys
import math
import itertools
import bisect
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
sys.setrecursionlimit(10**9)
mod = 10**9+7

N = i()
S = s()
a = 'S'
b = 'W'
kouho = [[a,a],[a,b],[b,a],[b,b]]
for a,b in kouho:
    S1 = [a,b]
    for i in range(1,N):
        if S[i] == 'o':
            if S1[i] == 'S':
                if S1[i-1] == 'S':
                    S1.append('S')
                else:
                    S1.append('W')
            else:
                if S1[i-1] == 'S':
                    S1.append('W')
                else:
                    S1.append('S')
        else:
            if S1[i] == 'S':
                if S1[i-1] == 'S':
                    S1.append('W')
                else:
                    S1.append('S')
            else:
                if S1[i-1] == 'S':
                    S1.append('S')
                else:
                    S1.append('W')
    if S1[-1] != a:
        continue
    S1 = S1[:N]
    if a == 'S' and b == 'S':
        if S[0] == 'o':
            if S1[-1] == 'S':
                print(''.join(S1))
                exit()
        else:
            if S1[-1] == 'W':
                print(''.join(S1))
                exit()
    elif a == 'S' and b == 'W':
        if S[0] == 'o':
            if S1[-1] == 'W':
                print(''.join(S1))
                exit()
        else:
            if S1[-1] == 'S':
                print(''.join(S1))
                exit()
    elif a == 'W' and b == 'S':
        if S[0] == 'o':
            if S1[-1] == 'W':
                print(''.join(S1))
                exit()
        else:
            if S1[-1] == 'S':
                print(''.join(S1))
                exit()
    else:
        if S[0] == 'o':
            if S1[-1] == 'S':
                print(''.join(S1))
                exit()
        else:
            if S1[-1] == 'W':
                print(''.join(S1))
                exit()
print(-1)
