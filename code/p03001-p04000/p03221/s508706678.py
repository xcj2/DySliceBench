import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, M = MAP()
PY = [LIST() for _ in range(M)]
PY_ = deepcopy(PY)
PY_.sort(key=lambda x: (x[0], x[1]))
# print(PY)
tmp = 0
i = 0
lis = []
dic = {}
for p, y in PY_:
	if p == tmp:
		i += 1
	else: # 県が変わったら
		lis.append([])
		tmp = p
		i = 1
	dic[str(p)+"_"+str(y)]=str(p).zfill(6)+str(i).zfill(6)

for p, y in PY:
	print(dic[str(p)+"_"+str(y)])
