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
		n,q=num()
		s=input()
		ff=[0]*n
		for i in range(n-1):
			if(s[i]=="A" and s[i+1]=="C"):
				ff[i]=1
		for i in range(1,n):
			ff[i]=ff[i-1]+ff[i]
		for i in range(q):
			l,r=num()
			l-=1
			r-=1
			if(s[r]=="A"):
				r-=1
			if(l==0):
				print(ff[r])
			else:
				print(ff[r]-ff[l-1])







if __name__ == "__main__":
	solve ()