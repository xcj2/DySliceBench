import collections
import itertools
import numpy as np
import sys
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

A,B,C,D = [i for i in S()]
s = A
l = [B,C,D]
for i in range(1 << len(l)):
	num = int(A)
	data = []
	for j in range(len(l)):
		if ((i >> j) & 1) == 1:
			num += int(l[j])
		else:
			num -= int(l[j])
	if num == 7:
		for j in range(len(l)):
			if ((i >> j) & 1) == 1:
				s += "+"+l[j]
			else:
				s += "-"+l[j]
		else:
			print(s+"=7")
			exit()