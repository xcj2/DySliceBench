# import bisect
# import heapq
# import math
# import random
# from collections import Counter, defaultdict, deque
# from decimal import Decimal
# from functools import lru_cache, reduce
# from itertools import combinations, combinations_with_replacement, product, permutations
# from operator import add, mul, sub, itemgetter
# import numpy as np

import sys
sys.setrecursionlimit(10000)

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

def read_int(input=None):
	if input == None:
		input = sys.stdin.readline().strip()
	ret = [int(x) for x in input.split()]
	if len(ret) == 1:
		ret = ret[0]
	return ret

def read_float(input):
	if input == None:
		input = sys.stdin.readline().strip()
	ret = [float(x) for x in input.split()]
	if len(ret) == 1:
		ret = ret[0]
	return ret
	
def read_str(input):
	if input == None:
		input = sys.stdin.readline().strip()
	ret = [x for x in input.split()]
	if len(ret) == 1:
		ret = ret[0]
	return ret
		
def read_int(read=None):
	if read == None:
		read = sys.stdin.readline().strip()
	return int(read)

def read_int_n(read=None):
	if read == None:
		read = sys.stdin.readline().strip()
	return [int(x) for x in read.split()]

def read_float(read=None):
	if read == None:
		read = sys.stdin.readline().strip()
	return float(read)

def read_float_n(read=None):
	if read == None:
		read = sys.stdin.readline().strip()
	return [float(x) for x in read.split()]

def read_str(read=None):
	if read == None:
		read = sys.stdin.readline().strip()
	return str(read)

def read_str_n(read=None):
	if read == None:
		read = sys.stdin.readline().strip()
	return [str(x) for x in read.split()]	

@mt
def slv(*args):
	X.sort()
	
	'''
	Y = []
	for i in range(M-1):
		Y.append(X[i+1] - X[i])
	'''
	Y = [X[i+1] - X[i] for i in range(M-1)]
	Y.sort(reverse=True)
	
	ans = X[-1] - X[0]
	for y in Y[:N-1]:
		ans -= y
	
	return ans

if __name__ == '__main__':
	t = '''3 7
-10 -3 0 9 -100 2 17'''.splitlines()
	
	N, M = read_int_n()
	X = read_int_n()
	
	print(slv(N,M,X))
	