import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)


N,Q = map(int,input().split())
BIT = [0]*(N+1)

def add(loc,value):
    global N
    BIT[loc] += value

    loc += loc & -loc

    while loc <= N:
        BIT[loc] += value
        loc += loc & -loc


def getSum(loc):
    ret = BIT[loc]
    loc -= loc & -loc

    while loc > 0:
        ret += BIT[loc]
        loc -= loc & -loc

    return ret


def calc(left,right):
    return getSum(right)-getSum(left-1)


for _ in range(Q):
    command,left,right = map(int,input().split())

    if command == 0:
        add(left,right)
    else:
        print("%d"%(calc(left,right)))
