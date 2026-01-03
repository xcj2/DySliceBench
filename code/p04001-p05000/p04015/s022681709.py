mod = 10**9+7
import sys
import math
from collections import Counter, defaultdict, deque
import copy

# from itertools import product, permutations, combinations, combinations_with_replacement
# from itertools import accumulate
# from operator import itemgetter
# from bisect import bisect_left,bisect
# from heapq import heappop,heappush
# from math import ceil,floor
# from copy import deepcopy
# from heapq import heappop,heappush,heapify
# import heapq


# def combinations(n, r):
# 	return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# def gcd(a, b):
# 	if b == 0:
# 		return a
# 	else:
# 		return gcd(b, a%b)
 
# def lcm(a, b):
# 	return a // gcd(a, b) * b

# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
# c = Counter(l)

# d = defaultdict(int)

sys.setrecursionlimit(10 ** 6)

int1 = lambda x: int(x) - 1

# リストの要素を改行を挟んで表示する
p2D = lambda x: print(*x, sep="\n")
# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())

def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())

# 入力全てを整数に変換したものの配列を受け取る
# def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI(): return list(map(lambda x:int(x), sys.stdin.readline().split()))
def HI(): return list(map(lambda x:int(x)*(-1), sys.stdin.readline().split()))


N, A=MI()
X = LI()

X = [x-A for x in X]
d = defaultdict(int)
d[0] = 1
for x in X:
	# new_dic = defaultdict(int)
	for k,v in list(d.items()):
		d[k+x] = d[k+x]+v
	# new_dic[x] = d[x] + 1
	# d = new_dic
print(d[0]-1)





