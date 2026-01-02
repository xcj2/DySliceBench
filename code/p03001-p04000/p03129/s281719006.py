# import bisect
# import heapq
# import math
# import random
# from fractions import gcd
# from collections import Counter, defaultdict, deque
# from decimal import Decimal
# from functools import lru_cache, reduce
# from itertools import combinations, combinations_with_replacement, product, permutations
# from operator import add, mul, sub, itemgetter
# import numpy as np

import sys
sys.setrecursionlimit(10000)

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
def slv(N, K):
	if N+1 >= 2* K:
		ans = 'YES'
	else:
		ans = 'NO'
	return ans

def main():
	t = '''
	'''.splitlines()
	N, K = read_int_n()
	print(slv(N, K))

if __name__ == '__main__':
	main()