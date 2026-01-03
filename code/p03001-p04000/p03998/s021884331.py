import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
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
def stoq(s):
    q = deque()
    for i in range(len(s)):
        q.append(s[i])
    return q
class counter(dict):
    def __init__(self, *args):
        super().__init__(args)
    def add(self,x):
        self.setdefault(x,0)
        self[x] += 1

S = list(map(stoq,[input() for _ in range(3)]))
k = 0
while True:
    if len(S[k])==0:
        break
    c = S[k].popleft()
    k = ston(c)
print(ntos(k,'A'))