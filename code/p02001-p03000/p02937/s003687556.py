# kartikay26

from math import *
from collections import *
from itertools import *
from functools import *
from random import *
def getl(t=int): return [t(x) for x in input().split()]
def get(t=int): return t(input())
alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
alnum = lambda x: ord(x) - ord('a')

def main():
	a = input()
	b = input()
	n = len(a)
	next_ = [next_arr(alphabet[i], a) for i in range(26)]
	ptr = -1
	ans = 0
	for ch in b:
		old_ptr = ptr
		ptr = next_[alnum(ch)][ptr]
		if ptr == -1:
			print(-1)
			exit()
		if ptr <= old_ptr:
			ans += n
	print(ans+ptr+1)

def next_arr(ch, a):
	n = len(a)
	i = a.find(ch)
	if i == -1:
		return [-1] * n
	ret = [-1] * n
	while ret[prev(i,n)] == -1:
		if a[i] == ch:
			ret[prev(i,n)] = i
		else:
			ret[prev(i,n)] = ret[i]
		i = prev(i,n)
	return ret


def next(i, n):
	return (i+1) % n
def prev(i, n):
	return (i-1+n) % n

if __name__ == "__main__":
	main()
