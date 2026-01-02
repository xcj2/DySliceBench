import math
import itertools
from heapq import heapify, heappop, heappush
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque


# d = defaultdict(lambda: 0)
# setrecursionlimit(10**7)
# inf = float("inf")


##### stdin ####
def LM(t, r): return list(map(t, r))
def R(): return stdin.readline()
def RS(): return R().split()
def I(): return int(R())
def F(): return float(R())
def LI(): return LM(int,RS())
def LF(): return LM(float,RS())
def ONE_SL(): return list(input())
def ONE_IL(): return LM(int, ONE_SL())
def ALL_IL(): return LM(int,stdin)

##### tools #####
def ap(f): return f.append
def pll(li): print('\n'.join(LM(str,li)))
def pljoin(li, s): print(s.join(li))



##### main #####
def main():
	n = I()
	A = LI()
	A.append(0)

	prev = 0
	skip = []
	sum_all = 0

	for i in range(n):
		t1 = abs(prev - A[i])
		t2 = abs(A[i] - A[i+1])

		skipped = (t1+t2) - abs(prev - A[i+1])
		sum_all += t1

		skip.append(skipped)

		prev = A[i]
	sum_all += abs(A[n-1] - A[n])

	for s in skip:
		print(sum_all - s)

if __name__ == '__main__':
  main()