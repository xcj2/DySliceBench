import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub, itemgetter
import numpy as np

sys.setrecursionlimit(10000)

def read_int():
	return int(sys.stdin.readline().strip())

def read_int_n():
	return [int(x) for x in sys.stdin.readline().strip().split()]

def read_float():
	return float(sys.stdin.readline().strip())

def read_float_n():
	return [float(x) for x in sys.stdin.readline().strip().split()]

def read_str():
	return sys.stdin.readline().strip()

def read_str_n():
	return [str(x) for x in sys.stdin.readline().strip().split()]

def error_print(*args):
	print(*args, file=sys.stderr)

def mt(f):
	import time
	def wrap(*args, **kwargs):
		s = time.time()
		ret = f(*args, **kwargs)
		e = time.time()
		error_print(e - s, 'sec')
		return ret
	return wrap

@mt
def slv(N):
	S = 0
	for i in N:
		S += int(i)
		
	if int(N) % S == 0:
		ans = 'Yes'
	else:
		ans = 'No'
		
	return ans

def main():
	N = read_str()
	print(slv(N))

if __name__ == '__main__':
	main()