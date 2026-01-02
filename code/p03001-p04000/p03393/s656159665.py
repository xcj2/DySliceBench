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

	S = input()
	
	if S == 'zyxwvutsrqponmlkjihgfedcba':
		print(-1)
		exit()

	set_al = set([chr(i) for i in range(97,123)])
	set_s = set(S)

	if len(S) != len(set_s):
		print("-1")

	availables = sorted(list(set_al - set_s), reverse = True)

	if availables:
		print(S+str(availables[-1]))
	else:
		f = False
		for i in range(len(S))[::-1]:
			chr_n = ord(S[i])

			while chr_n <= 122:
				if chr(chr_n) not in S:
					S = S[:-1]
					S += chr(chr_n)
					f = True
					break
				chr_n += 1

			if f:
				break
			S = S[:-1]

		print(S)


if __name__ == '__main__':
  main()