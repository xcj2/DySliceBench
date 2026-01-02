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
		
@mt
def slv(*args): 
	# 処理
	# ここから
	
	if max(L) < sum(L) - max(L):
		ans = 'Yes'
	else:
		ans = 'No'
	
	# ここまで
	return ans

if __name__ == '__main__':
	
	# テスト用入力
	t = '''4
3 8 5 1'''.splitlines()
	
	# 入力 (変数= read_xxx(test[行数]))
	# ここから
	
	N = read_int()
	L = read_int()
	
	# ここまで
		
	# 出力
	# ここから
	
	print(slv(N, L))
	
	# ここまで