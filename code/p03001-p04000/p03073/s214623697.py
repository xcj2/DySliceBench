import math
import os
import random
import re
import sys
from collections import defaultdict

# sys.stdin = open('input.in', 'r')
# sys.stdout = open('output.out', 'w') 

def onezero(a):
	count = 0
	for i in range(0, len(a), 2):
		if a[i] == 0:
			count += 1
	for i in range(1, len(a), 2):
		if a[i] == 1:
			count += 1
	return count

def zeroone(a):
	count = 0
	for i in range(0, len(a), 2):
		if a[i] == 1:
			count += 1
	for i in range(1, len(a), 2):
		if a[i] == 0:
			count += 1
	return count


def count(n):
	return min(onezero(n),zeroone(n))

if __name__ == '__main__':
	N = [int(d) for d in input()]
	print(count(N))