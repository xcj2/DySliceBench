import math
import itertools
import heapq
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
def ALL_I(): return map(int, stdin)
def ALL_IL(): return LM(int,stdin)

##### tools #####
def ap(f): return f.append
def pll(li): print('\n'.join(LM(str,li)))
def pljoin(li, s): print(s.join(li))



##### main #####		
def main():
	N,K = LI()
	A = LI()

	cnt_d=defaultdict(lambda: 0)
	for i in A:
		cnt_d[i] += 1
	
	sorted_d = sorted(cnt_d.items(), key=lambda x: x[1])
	
	ans=0
	i=0
	n = len(cnt_d)
	while n>K:
		min_k,min_v = sorted_d[i]
		i+=1
		ans+=min_v
		n-=1

	print(ans)


if __name__ == '__main__':
	main()