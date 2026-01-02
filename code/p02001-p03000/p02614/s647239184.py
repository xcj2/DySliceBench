import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from itertools import product
import copy

H,W,K = LI()
c = [list(map(str,input())) for _ in range(H)]

def count(S):
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    return ans

A = list(product([True,False],repeat=H))
B = list(product([True,False],repeat=W))

num = 0
for a in A:
    for b in B:
        S = copy.deepcopy(c)
        for i in range(H):
            if a[i]:
                for j in range(W):
                    S[i][j] = '?'
        for j in range(W):
            if b[j]:
                for i in range(H):
                    S[i][j] = '?'
        co = count(S)
        if co == K:
            num += 1

print(num)