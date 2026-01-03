import sys
import numpy as np
import random
from decimal import Decimal
import itertools
import re
import bisect
from collections import deque, Counter
from functools import lru_cache

sys.setrecursionlimit(10**9)
INF = 10**13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
def SERIES(n): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ')
def GRID(h,w): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ').reshape(h,-1)[:,:w]
def GRIDfromString(h,w): return np.frombuffer(sys.stdin.buffer.read(), 'S1').reshape(h,-1)[:,:w]
MOD = 1000000007

def main():
	h, w, n = LI()
	black_points = []
	for i in range(n):
		a, b = LI()
		add_list = ((a-2,b-2),(a-2,b-1),(a-2,b),(a-1,b-2),(a-1,b-1),(a-1,b),(a,b-2),(a,b-1),(a,b))
		for c, d in add_list:
			if 1 <= c <= h-2 and 1 <= d <= w-2:
				black_points.append((c,d))
	counter = Counter(black_points)
	count_list = list(counter.values())
	counter2 = Counter(count_list)
	ans_list = [counter2[i] for i in range(1,10)]
	ans_list = [(h-2)*(w-2)-sum(ans_list)] + ans_list
	for ans in ans_list:
		print(ans)



if __name__ == '__main__':
    main()