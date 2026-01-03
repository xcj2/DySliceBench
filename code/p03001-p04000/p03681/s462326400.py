import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
from functools import reduce
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
def lgcd(l):
    return reduce(gcd,l)
def llcm(l):
    return reduce(lcm,l)
def perm(n,mod=None):
    ans = 1
    for i in range(1,n+1):
        ans *= i
        if mod!=None:
            ans %= mod
    return ans
def intput():
    return int(input())
def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)
def ston(c, c0='a'):
    return ord(c)-ord(c0)
def ntos(x, c0='a'):
    return chr(x+ord(c0))
class counter(dict):
    def __init__(self, *args):
        super().__init__(args)
    def add(self,x):
        self.setdefault(x,0)
        self[x] += 1

N,M = mint()
if abs(N-M)>1:
    print(0)
else:
    ans = perm(N,MOD)*perm(M,MOD)*(2-abs(N-M))
    print(ans%MOD)