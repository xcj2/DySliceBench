import random, math
from copy import deepcopy as dc
from bisect import bisect_left, bisect_right



# Function to call the actual solution
def solution(li):
	ma = {}
	for i in li:
		ma[i] = ma.get(i, 0) + 1
	s = 0
	for i in ma:
		if i != ma[i]:
			if ma[i] > i:
				s += ma[i] - i
			else:
				s += ma[i]
	return s


# Function to take input
def input_test():
	# for _ in range(int(input())):
		n = int(input())
		# a, b = map(int, input().strip().split(" "))
		# a, b, c = map(int, input().strip().split(" "))
		li = list(map(int, input().strip().split(" ")))
		out = solution(li)
		print(out)

# Function to check test my code
def test():
	pass


input_test()
# test()