mod = 10**9+7
import sys
from collections import Counter, defaultdict, deque
from itertools import product, permutations, combinations, combinations_with_replacement
from itertools import accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush
from math import ceil,floor
from copy import deepcopy
from heapq import heappop,heappush,heapify
import heapq


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



# n = II()
# p = tuple(MI())
# q = tuple(MI())

# l = list(permutations(list(range(1,n+1))))
# print(abs(l.index(p)-l.index(q)))
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)
 
def lcm(a, b):
	return a // gcd(a, b) * b
 
N, M = MI()
A = LI()
A = [a//2 for a in A]


while A[0] % 2 == 0:
	for i in range(N):
		if A[i] % 2 != 0:
			print(0)
			exit()
		A[i] //= 2
	M //= 2

 
for i in range(N):
	if A[i] % 2 == 0:
		print(0)
		exit()
 
tmp_lcm = 1
for i in range(N):
	tmp_lcm = lcm(tmp_lcm, A[i])
	if M < tmp_lcm:
		print(0)
		exit()
 
print((M // tmp_lcm + 1) // 2)