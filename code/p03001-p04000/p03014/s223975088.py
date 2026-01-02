# ANSHUL GAUTAM
# IIIT-D

from math import *
from copy import *					# ll = deepcopy(l)
from heapq import *					# heappush(hp,x)
from string import *				# alpha = ascii_lowercase
from random import *				# l.sort(key=lambda l1:l1[0]-l1[1]) => ex: sort on the basis difference
from bisect import *				# bisect_left(arr,x,start,end)  => start and end parameters are temporary
from sys import stdin				# bisect_left return leftmost position where x should be inserted to keep sorted
from sys import maxsize				# minn = -maxsize
from operator import *				# d = sorted(d.items(), key=itemgetter(1))
from itertools import *				# pre = [0] + list(accumulate(l))
from decimal import Decimal 		# a = Decimal(a)	# use this for math questions
from collections import Counter		# d = dict(Counter(l))
from collections import defaultdict # d = defaultdict(list)

'''
4 6
#..#..
.....#
....#.
#.#...
'''

def transpose(m):
	rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
	return rez

def giveLightIntervals(L,h,w):
	l = [[] for i in range(h)]
	for i in range(h):
		s,e,c = '','',0
		for j in range(w):
			if(L[i][j] == '#'):
				if(c > 0):
					e = j
					l[i].append([s,e-1])
					c = 0
				s,e = '',''
			else:
				if(s == ''):
					s = j
				c += 1
		if(L[i][-1] == '.'):
			l[i].append([s,w-1])
	return l

def solve(L,h,w):
	T = transpose(L)
	l = giveLightIntervals(L,h,w)
	t = giveLightIntervals(T,w,h)

	H = [[0 for i in range(w)] for j in range(h)]
	W = [[0 for i in range(h)] for j in range(w)]

	for i in range(h):
		zz = 0
		for j in range(w):
			if(len(l[i]) > zz):
				s,e = l[i][zz]
				val = e - s + 1
				if(s <= j <= e):
					H[i][j] = val
				if(j == e):
					zz += 1
			else:
				break

	for i in range(w):
		zz = 0
		for j in range(h):
			if(len(t[i]) > zz):
				s,e = t[i][zz]
				val = e - s + 1
				if(s <= j <= e):
					W[i][j] = val
				if(j == e):
					zz += 1
			else:
				break

	ans = 0

	for i in range(h):
		for j in range(w):
			curr = H[i][j] + W[j][i] - 1
			ans = max(ans,curr)

	return ans


H,W = list(map(int, stdin.readline().rstrip().split()))
L = []
for m in range(H):
	L.append(list(input()))
ans = solve(L,H,W)
print(ans)

