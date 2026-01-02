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


n,m = MI()
h = LI()
a = []

d = defaultdict(int)
for _ in range(m):
	aa,bb = MI()
	d[(aa-1)] = max(d[bb-1],d[(aa-1)])
	d[(bb-1)] = max(d[bb-1],d[(aa-1)])
	if not aa==bb:
		if h[aa-1]>=h[bb-1]:
			a.append(bb-1)
		if h[bb-1]>=h[aa-1]:
			a.append(aa-1)

print(n-len(set(a)))
# ans=0
# for i in range(n):
# 	if h[i]<=d[i]:
# 		ans += 0
# 	else:
# 		ans += 1
	# tmp = d[str(h[i])]
	# k = 1
	# if len(tmp)>0:
	# 	tmp = [int(s) for s in tmp.split(':') if not s=='']
	# 	for s in tmp:
	# 		if int(h[i])<=s:
	# 			k = 0
	# ans+=k
# print(ans)














