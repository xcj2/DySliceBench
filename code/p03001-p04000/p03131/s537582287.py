# import bisect
# import heapq
# import math
# import random
# from fractions import gcd
# from collections import Counter, defaultdict, deque
from decimal import Decimal
import decimal
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
def slv(K, A, B):
	if B - A <= 2:
		ans = K + 1
	else:
		if (K - A + 1) % 2 ==0:
			ans = (B-A)*(Decimal(str(K-A+1))/Decimal('2'))+A
		else:
			ans = (B-A)*(Decimal(str(K-A))/Decimal('2'))+A+1
	return ans

def main():
	t = '''4 2 6'''.splitlines()
	K, A, B = read_int_n()
	print(slv(K, A, B))

if __name__ == '__main__':
	main()