import io, sys, atexit, os

import math as ma
from sys import exit
from decimal import Decimal as dec
from itertools import permutations


def li ():
	return list (map (int, input ().split ()))


def num ():
	return map (int, input ().split ())


def nu ():
	return int (input ())


def find_gcd ( x, y ):
	while (y):
		x, y = y, x % y
	return x


mm = 1000000007



def solve ():
	t = 1
	for it in range (t):
		n,m=num()
		x=[]
		for i in range(n):
			l,r=num()
			x.append((l,r))
		x.sort()
		cc=m
		cost=0
		for i in range(n):
			cost+=x[i][0]*min(cc,x[i][1])
			cc-=min(cc,x[i][1])
		print(cost)






if __name__ == "__main__":
	solve ()