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

N,H = IL()
ab = [IL() for i in range(N)]

ab.sort(reverse=True)
attack = ab[0][0]
skill = ab[0][1]

ab.sort(reverse=True,key=itemgetter(1))
cnt = 0
f = 0
for i in range(N):
	if ab[i][1] > attack:
		H -= ab[i][1]
		cnt += 1
	if H <= 0:
		print(cnt)
		exit()

print(cnt + math.ceil(H/attack))