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

'''

def primeFactorization(x):
	d = defaultdict(int)
	d[1] = 0
	while(x%2 == 0):
		x //= 2
		d[2] += 1
	for i in range(3,int(sqrt(x))+1,2):
		while(x%i == 0):
			d[i] += 1
			x //= i
	if(x > 2):
		d[x] += 1
	return d

def Sieve(x):
	checkPrime = [1 for i in range(x+1)]
	zz = 2
	L = []
	while(zz**2 <= x):
		if(checkPrime[zz] == 1):
			for i in range(zz*2,x+1,zz):
				checkPrime[i] = 0
		zz += 1
	for i in range(2,x):
		if(checkPrime[i] == 1):
			L.append(i)
	return L
	# return checkPrime

# print(len(Sieve(int(sqrt(10**7))+1)))


def solve(x):
	check = [0]*(x+1)
	for i in range(1,x+1):
		j = 1
		while(i*j < x+1):
			check[i*j] += 1
			j += 1
	ans = 0
	# print(check)
	for i in range(1,x+1):
		ans += i * check[i]
	return ans

N = int(stdin.readline())
ans = solve(N)
print(ans)

