from sys import stdin, stdout
import heapq
import cProfile
from collections import Counter, defaultdict, deque
from functools import reduce
import math
import threading
import sys
import time


def get_int(): return int(stdin.readline().strip())


def get_tuple(): return map(int, stdin.readline().split())


def get_list(): return list(map(int, stdin.readline().split()))

n = get_int()
ls = []
for _ in range(n):
    x,y = get_tuple()
    ls.append([x,y])

one,two,three = False,False,False
one = True if ls[0][0]==ls[0][1] else False
two = True if ls[1][0]==ls[1][1] else False
three = True if ls[2][0]==ls[2][1] else False
flag = 0
for i in range(3,n):
    one = two; two=three
    three = True if ls[i][0]==ls[i][1] else False
    if one and two and three:
        flag = 1
        break
if one and two and three:
        flag = 1
if flag: print("Yes")
else: print("No")