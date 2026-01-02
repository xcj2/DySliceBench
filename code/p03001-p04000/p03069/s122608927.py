import math
from operator import itemgetter
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
s = S()

a = s.count("#")
b = s.count(".")
cnta = 0
cntb = 0
ans = MAX_INT
for i in range(N):
	if s[i] == "#":
		ans = min(ans,cnta + (b-cntb))
		cnta += 1
	else:
		cntb += 1
if ans == MAX_INT:
	print(0)
else:
	print(min(ans,a,b))