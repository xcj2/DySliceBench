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
def ALL_IL(): return LM(int,stdin)

##### tools #####
def ap(f): return f.append
def pll(li): print('\n'.join(LM(str,li)))
def pljoin(li, s): print(s.join(li))



##### main #####

def main():
	cx = 0; cy = 0
	prev_t = 0

	for i in range(I()):
		t, dist_x, dist_y = LI()

		diff = abs(dist_x - cx) + abs(dist_y - cy)		
		spend_time = t - prev_t


		if spend_time >= diff and (spend_time - diff)%2 == 0:
			f = True
		else:
			f = False
			break

		prev_t = t
		cx = dist_x
		cy = dist_y
	
	if f:
		print("Yes")
	else:
		print("No")

if __name__ == '__main__':
	main()