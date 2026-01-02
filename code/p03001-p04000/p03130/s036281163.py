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
def slv(A):
	ans = 'YES'
	for i in range(1, 5):
		if A.count(i) > 2:
			ans = 'NO'
	return ans

def main():
	t = '''2 1
	3 2
	4 3'''.splitlines()
	
	a1, b1 = read_int_n()
	a2, b2 = read_int_n()
	a3, b3 = read_int_n()
	A = [a1, b1, a2, b2, a3, b3]
	
	print(slv(A))

if __name__ == '__main__':
	main()