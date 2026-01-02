import sys
from functools import lru_cache

sys.setrecursionlimit(10**3)

import math

n = 0
k = 0

def format_input(filename = None):
	global n
	global k
	if filename == None:
		n = list(map(int, input().split())).pop()
		k = list(map(int, input().split())).pop()

	elif filename == '__random__':
		from random import randint as rng
		n = rng(1, 10**100)
		k = rng(1, 3)

@lru_cache(maxsize=None)
def comb_rec(n, k, digits):
	if digits < k - 1:
		return 0
	if k == 0:
		return 1
	if digits == 0:
		return n
	top = n // 10 ** digits
	if top == 0:
		combination = comb_rec(n, k, digits - 1)
	elif top == 1:
		combination = comb_rec(n - 10 ** digits, k - 1, digits - 1)
		combination += comb_rec(10 ** digits - 1, k, digits - 1)
	else:
		combination = comb_rec(n - top * 10 ** digits, k - 1, digits - 1)
		combination += (top - 1) * comb_rec(10 ** digits - 1, k - 1, digits - 1)
		combination += comb_rec(10 ** digits - 1, k, digits - 1)
	return combination


def get_answer():
	digits = math.floor(math.log10(n))
	answer = comb_rec(n, k, digits)
	return answer

if __name__ == '__main__':
	format_input()

	ans = get_answer()
	print(ans)
