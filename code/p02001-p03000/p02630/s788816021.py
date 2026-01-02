#!/usr/bin/env pypy
 
import sys
import string
from collections import Counter

def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split()) 
def get_list(): return list(map(int, sys.stdin.readline().strip().split())) 
def get_string(): return sys.stdin.readline().strip()
def out(data): return sys.stdout.write(str(data))
def out_list(arr): return sys.stdout.write(' '.join(str(e) for e in arr))

MAX = 10**9
MOD = 10**9 + 7

n = get_int()
arr = get_list()
d = Counter(arr)
q = get_int()
sum_ = sum(arr)

for _ in range(q):
	a, b = get_ints()
	if a in d.keys() :
		sum_ += d[a] * (b - a)
		count = d[a]
		d.pop(a)
		if not d[b]:
			d[b] = count
		else:
			d[b] += count
	out(sum_)
	out('\n')


