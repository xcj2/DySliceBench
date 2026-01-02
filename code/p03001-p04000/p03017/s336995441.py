import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
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

N,A,B,C,D = mint()
S = input()

def f(m,n):
    block2 = space3 = False
    b = s = 0
    for i in range(m-1,n):
        (b,s) = (b+1,0) if S[i]=='#' else (0,s+1)
        if not block2 and b==2:
            block2 = True
        if not space3 and s==3:
            space3 = True
    return block2, space3

if D<C:
    judge(not f(A,C)[0] and f(B-1,D+1)[1])
else:
    judge(not f(A,C)[0] and not f(B,D)[0])