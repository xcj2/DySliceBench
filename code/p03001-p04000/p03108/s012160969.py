# coding: UTF-8
import sys
#sys.setrecursionlimit(n)
import heapq
import re
import bisect
import random
import math
import itertools
from collections import defaultdict, deque
from copy import deepcopy
from decimal import *

def find(x):
    if node[x] < 0:
        return x
    else:
        node[x] = find(node[x])
        return node[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    ret = False
    if x != y:
        ret = True
        if rank[x] > rank[y]:
            node[x] += node[y]
            node[y] = x
        else:
            node[y] += node[x]
            node[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    return ret

def is_same(x, y):
    return find(x) == find(y)

def size(x):
    return -node[find(x)]

n, m = map(int,input().split())
node = [-1 for i in range(n + 1)]
rank = [0 for i in range(n + 1)]
e = [[int(i) for i in input().split()] for i in range(m)]
ans = deque()
num = int((n * (n - 1)) // 2)
s = 0
for i in e[::-1]:
    s1 = size(i[0])
    s2 = size(i[1])
    ans.appendleft(num)
    if unite(i[0], i[1]):
        num -= s1 * s2
for i in ans:
    print(i)
