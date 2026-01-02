import sys
read = sys.stdin.buffer.read
input=lambda :sys.stdin.readline().rstrip()
inputs= sys.stdin.buffer.readlines
INF=float("inf")
MOD=10**9+7
#input = sys.stdin.buffer.readline
sys.setrecursionlimit(2147483647)
#rstrip().decode('utf-8')
#import math
#import numpy as np
#import operator
#import bisect
#from heapq import heapify,heappop,heappush
#from math import gcd
#from fractions import gcd
#from collections import deque
#from collections import defaultdict
#from collections import Counter
#from itertools import accumulate
#from itertools import groupby
#from itertools import permutations
#from itertools import combinations
#from scipy.sparse import csr_matrix
#from scipy.sparse.csgraph import floyd_warshall
#from scipy.sparse.csgraph import csgraph_from_dense
#from scipy.sparse.csgraph import dijkstra
#map(int,input().split())
#from scipy.special import comb

def framod(n, mod, a=1):
	for i in range(1, n + 1):
		a = a * i % mod
	return a


def power(n, r, mod):
	if r == 0: return 1
	if r % 2 == 0:
		return power(n * n % mod, r // 2, mod) % mod
	if r % 2 == 1:
		return n * power(n, r - 1, mod) % mod


def comb(n, k, mod):
	a = framod(n, mod)
	b = framod(k, mod)
	c = framod(n - k, mod)
	return (a * power(b, mod - 2, mod) * power(c, mod - 2, mod)) % mod


def main():
	X,Y=map(int,input().split())
	
	a=max(X,Y)
	b=min(X,Y)
	
	ans=0
	
	t=2*a-b
	
	
	if t%3==0 and t>0 and a<=b*2:
		c1=t//3
		c2=a-2*t//3
		ans=comb(c1+c2,c1,MOD)
		
	print(ans)
		
	
	
	
	
if __name__ == '__main__':
	main()