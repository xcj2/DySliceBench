import sys
from math import factorial
from collections import Counter
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

n, m, x = MAP()
bene = [[0]*(m+1) for i in range(n)]
for i in range(n):
    a = LIST()
    bene[i] = a

def add(in1, in2):
    return [a + b for a, b in zip(in1, in2)]

bene = sorted(bene)
result = []
for n in range(1,len(bene)+1):
    for conb in itertools.combinations(bene, n):
        conb = list(conb)
        res = conb[0]
        for i in range(len(conb)-1):
            res = add(res, conb[i+1])
        result.append(res) 
result = sorted(result)

for i in range(len(result)):
    flag = True
    for j in range(m):
        if result[i][j+1] <x:
            flag = False
    if flag:
        print(result[i][0])
        sys.exit()
print(-1)