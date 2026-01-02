import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

c = [lint() for _ in range(3)]
judge(
    c[0][0]-c[0][1]==c[1][0]-c[1][1]==c[2][0]-c[2][1] and
    c[0][0]-c[0][2]==c[1][0]-c[1][2]==c[2][0]-c[2][2] and
    c[0][1]-c[0][2]==c[1][1]-c[1][2]==c[2][1]-c[2][2] and
    c[0][0]-c[1][0]==c[0][1]-c[1][1]==c[0][2]-c[1][2] and
    c[0][0]-c[2][0]==c[0][1]-c[2][1]==c[0][2]-c[2][2] and
    c[2][0]-c[1][0]==c[2][1]-c[1][1]==c[2][2]-c[1][2]
)